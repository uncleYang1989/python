
############################################
###             准备工作                  ###
############################################
#将/var/lib/mysql整个文件夹备份，例如备份到/root/install/jyang目录下，用于auto的python脚本自动修复
#通过cat /commsky/etc/sky.properties | grep version ，获得版本号，然后通过编译环境获得对于的安装包。
#将数据库的sql文件准备好

############################################
###删除历史的mysql（请在mysql备份后操作！！！）###
############################################
yum -y remove mysql*
yum -y remove MySQL*
#删除mysql相关文件
rm -rf /var/lib/mysql
rm -rf /usr/include/mysql
rm -rf /usr/lib/mysql
rm -rf /usr/share/mysql
rm -rf /usr/lib64/mysql
rm -rf /var/lock/subsys/mysql
rm -rf ~/.mysql_secret

#####或者用另外一种删除方式#####
yum remove  mysql mysql-server mysql-libs mysql-server;
find / -name mysql #将找到的相关东西delete掉；
rpm -qa|grep mysql#(查询出来的东东yum remove掉)

#!!!!!!!!!!!!!!!!!!!!!!!碰到安装数据库中途关机导致无法正常安装!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##今天强制重启了 Fedora 15，结果开机之后在 yum update 就报错了，
##最后就是：
##TypeError: rpmdb open failed
##估计是非正常关机引起的，g了一下，解决方法如下：
##首先清除掉缓存，之后再重建就可以了，第二步的重建可以不做，估计yum会自动生成
##rm -f /var/lib/rpm/__db*
##rpm --rebuilddb
##之后再执行 yum update ，重新生成 presto, 正常更新。
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


############################################
###            重新安装mysql              ###
############################################
#重新安装mysql，请切换到安装包的rpm目录下操作
yum -y localinstall --disablerepo=* MySQL*.rpm --nogpgcheck
#或者用另外一种安装方式
yum install  mysql mysql-server mysql-libs mysql-server;

#设置自启动
chkconfig --level 2345 mysql on


############################################
###            恢复数据                    ###
############################################
#修改默认密码commsky
cat ~/.mysql_secret |grep random|cut -d: -f4-|sed 's| ||g'|tail -1
mysqladmin -uroot -p密码 password c0mm3ky
mysqladmin -uroot -pIPSLfPNY password c0mm3ky
#创建commsky用户
mysql -uroot -pc0mm3ky -e "CREATE USER 'commsky'@'localhost' IDENTIFIED BY 'c0mm3ky';"
#创建相关数据库nms／auth
mysql -uroot -pc0mm3ky -e "CREATE DATABASE IF NOT EXISTS commsky_nms;GRANT ALL ON commsky_nms.* TO 'commsky'@'localhost' IDENTIFIED BY 'c0mm3ky';FLUSH PRIVILEGES;"
mysql -uroot -pc0mm3ky -e "CREATE DATABASE IF NOT EXISTS commsky_auth;GRANT ALL ON commsky_auth.* TO 'commsky'@'localhost' IDENTIFIED BY 'c0mm3ky';FLUSH PRIVILEGES;"

#1 直接导入备份的数据 （适用于在自己搭建的环境里恢复完成的操作）
#导入commsky_nms恢复数据
mysql -f commsky_nms -ucommsky -pc0mm3ky< /root/install/jyang/data/backup_commsky_nms.sql
#导入commsky_auth恢复数据
mysql -f commsky_auth -ucommsky -pc0mm3ky< /root/install/jyang/data/backup_commsky_auth.sql


#2直接在现场恢复
#切换到安装包解压后的all-install/db目录下
mysql -f commsky_nms -ucommsky -pc0mm3ky< nms/db_schema.sql
mysql -f commsky_nms -ucommsky -pc0mm3ky< nms/db_data.sql

mysql -f commsky_auth -ucommsky -pc0mm3ky< auth/db_schema.sql
mysql -f commsky_auth -ucommsky -pc0mm3ky< auth/db_data.sql
#使用自动化脚本automysql.py恢复
python automysql.py



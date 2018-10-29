#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月30日

@author: jyang
'''

from aliyun.usermgt.usermgtUtil import *
from aliyun.usermgt import HOSTNAME, APPNAME, USERS
from aliyun.usermgt.dep.createDefaultPerms import *
import  pinyin
pinyin.get
def domainperms():
    domains = [
[[1,1,1,0],u'全市域','domain:hang2zhou1shi4quan2yu4','b25c50e1e9dba3e6af2d0acf4b9533a5;全市域;10;3'],
[[1,1,0,0],u'市区','domain:shi2cheng2qu1','c52d33de1c3f61330bf198b92c6e9c45;市区;20;3'],
[[1,1,0,1],u'主城区据','domain:liu4cheng2qu1','ffedf6c1c30a48c3946bb7c2273651e9;主城区;30;1'],
[[0,0,1,0],u'指挥中心','domain:zhihuizhongxin','00000000000000000000000000000000;指挥中心;14;0'],
[[0,0,1,0],u'信号配时中心','domain:xinhaopeishi','00000000000000000000000000000000;信号配时中心;18;0'],
[[1,1,1,1],u'上城','domain:shang4cheng2da4dui4','6301f9905d6ffa1412ac94c82a6e79ab;上城大队;40;2'],
[[1,1,1,1],u'下城','domain:xia4cheng2da4dui4','16c0ea42c2ec7bf092f87abb4a5d3924;下城大队;50;2'],
[[1,1,1,1],u'西湖','domain:xi1hu2da4dui4','2fc5e60107ebdbca0d036ad2f2e2671f;西湖大队;60;2'],
[[1,1,1,1],u'江干','domain:jiang1gan1da4dui4','efbbe65ee090be44c43d6abc651c9db5;江干大队;70;2'],
[[1,1,1,1],u'拱墅','domain:gong3shu4da4dui4','ebbd32f29fd5497bb562578ee56eb750;拱墅大队;80;2'],
[[1,1,1,1],u'滨江','domain:bin1jiang1da4dui4','ebe1ff7e9ba13167dde50b4b1fb238ac;滨江大队;90;2'],
[[1,1,1,1],u'下沙','domain:xia4sha1da4dui4','6767c2b7de2284b9bfaad561007efcd2;下沙大队;100;2'],
[[1,1,1,0],u'高架','domain:gao1jia4da4dui4','7bf53803e110904f76f0268ebba7742e;高架大队;110;5'],
[[1,1,1,0],u'绕城','domain:rao4cheng2da4dui4','5f72cd90551e21fee79a57c88c02c5e1;绕城大队;120;6'],
[[1,1,1,1],u'景区','domain:jing3qu1da4dui4','baddbf886e3cb1bbdd6faef29f70d380;景区大队;130;2'],
[[1,1,1,0],u'大江东','domain:da4jiang1dong1da4dui4','bf89db7c6bca207dc0da6715dee1426d;大江东大队;140;4'],
[[1,1,1,0],u'萧山','domain:xiao1shan1da4dui4','d9ff8785ee954676e58c4c8f87069942;萧山大队;150;4'],
[[1,1,1,0],u'余杭','domain:yu2hang2da4dui4','2b5fb1dccfb3325b034ed443a3489520;余杭大队;160;4'],
[[1,1,1,0],u'富阳','domain:fu4yang2da4dui4','ab3475fd39c845022df5ee9b1415087a;富阳大队;170;4'],
[[1,1,1,0],u'临安','domain:lin2an1da4dui4','4b2ed4f5d4853506afbadaaf25bc8d63;临安大队;180;4'],
[[1,1,1,0],u'桐庐','domain:tong2lu2da4dui4','a52a141ddabf96f18282491511096c5e;桐庐大队;190;4'],
[[1,1,1,0],u'淳安','domain:chun2an1da4dui4','bdc6a5b7d58c9af5add3fb5728caba9c;淳安大队;200;4'],
[[1,1,1,0],u'建德','domain:jian4de2da4dui4','26420f1fdfe4d8810e0356a9097ec4d5;建德大队;210;4'],
        ]
    #[大屏、公众服务、警情处置、重点车辆]
    allDomains = []
    datavDomains = []
    uppsDomains = []
    evtDomains = []
    verDoamins = []
    for mark, name, code, desc in domains:
        print desc.split(";")[0]
        if mark[0]:
            datavDomains.append([u"datav-" +name, code, desc]);
        if mark[1]:
            uppsDomains.append([u"upps-" +name, "upps"+code, desc]);
        if mark[2]:
            evtDomains.append([u"evt-" +name, "evt"+code, desc]);
        if mark[3]:
            verDoamins.append([u"ver-" +name, "ver"+code, desc]);
    allDomains.extend(datavDomains);
    allDomains.extend(uppsDomains);
    allDomains.extend(evtDomains);
    allDomains.extend(verDoamins);
    return allDomains
def getUiPerms():
    perms = []
    data = {
        u"datav;态势大屏":[u"detail;详细信息"],
        u"upps;公众服务":[
                u"page:manual;审核发布",
                u"page:auto;自动发布          " ,
                u"page:media;媒体警情         " ,
                u"page:setting;设置管理       " ,
                u"page:statistics;统计分析    " ,
                u"page:info-type;信息类型管理     " ,
                u"page:si;信息接口管理            " ,
                u"page:author;互联网系统授权        " ,
                u"page:bcsetting;定时播报管理     " ,
                u"page:log;日志管理           " ,
                u"page:escort;一路护航身份管理        " ,
                u"page:template;文案模版管理     " ,
                u"op:msg:edit;信息编辑",
                u"op:msg:examine;信息审核     " ,
                u"op:suggest:reply;媒介警情处置"
                 ],
        u"event_handle;警情处置":[
                u"page:area;自定义区域         ",
                u"page:settings;配置管理     ",
                u"page:handle;警情处置       ",
                u"page:query;警情查询        ",
                u"page:statis;统计分析       ",
                u"op:home:handle;警情处置    ",
                u"op:home:message;消息通知按钮   ",
                ],
        u"vehicles;重点车辆":[
                u"page:realtime;实时报警        ",
                u"page:evt;事件查询     ",
                u"page:analyse;规律分析       ",
                u"page:config;参数配置        "
                ],
        u"data_monitor;数据监控":[],
        u"sys_operation;云资源运维平台":[],
        u"quick_bi;数据魔方":[],
        u"user_mgt;权限管理":[
            u"page:perm;权限管理",
            u"page:role;角色管理",
            u"page:org;组织管理",
            u"page:user;用户管理",
            u"super:admin;顶级管理员",
            u"data:admin;全部组织树查看",
            ],
        }

    for key in data.keys():
        name = key.split(";")[1];
        appName = key.split(";")[0]
        perms.append([unicode(name)+u"登录",u"ui:" + appName,u""])
#         print unicode(name)+u"应用进入权限"
        controls = data[key];
        for control in controls:
            if control.strip().split(";")[0].startswith("page"):
                cname = name+"-" + u"页面-" + control.strip().split(";")[1];
            elif control.strip().split(";")[0].startswith("op"):
                cname = name+"-" + u"操作-" + control.strip().split(";")[1];
            else:
                cname = name+"-" + u"其他-" + control.strip().split(";")[1];
            perms.append([cname,"ui:" + appName + ":" + control.strip().split(";")[0],""]);
#             print name+"-" + control.strip().split(";")[1]+ u"权限"
    return perms

def importPerms():
    perms = [];
    perms.extend(getUiPerms())
    perms.extend(domainperms())
#     for permTmp in perms:
#         print permTmp[0].encode('utf-8')
#         print createPermit(HOSTNAME, APPNAME, permTmp[0].encode('utf-8'), code=permTmp[1],desc=permTmp[2]);

if __name__ =="__main__":
    importPerms()
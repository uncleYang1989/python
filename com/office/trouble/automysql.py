#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import commands
import sys
from os import system
from os.path import join
RECOVER_DB_PATH = "/jyang";
DEST_SQL_PATH = "/jyang/backup";
MYSQL_DB_USER = "root"
MYSQL_DB_PASSWORD = "c0mm3ky"
RUN=False
databases = ["commsky_nms", "commsky_auth"];
result = {};
def execu(cmd, exitOnErr = True, printErrLog = True):
    print "cmd : " , cmd
    sts, text = commands.getstatusoutput(cmd)
    if sts != 0:
        if printErrLog:
            print "ERROR : ", sts, text
        if exitOnErr:
            sys.exit(sts);
    return sts, text

for database in databases:
    databasePath = join(RECOVER_DB_PATH, database);
    sts, text = execu("ls %s" % databasePath)
    names = set(text.replace("\n", " ").replace("db.opt", "").replace(r".ibd", "").replace(r".frm", "").replace("  ", " ").split(" "));
    result[database] = names;

template = """
mysql -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME -e "ALTER TABLE $TABLE_NAME DISCARD TABLESPACE;"
cp -f $RECOVER_DB_PATH/$DB_NAME/$TABLE_NAME.ibd /var/lib/mysql/$DB_NAME/
chown mysql:mysql /var/lib/mysql/$DB_NAME/*
chmod g+w /var/lib/mysql/$DB_NAME/*
mysql -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME -e "ALTER TABLE $TABLE_NAME IMPORT TABLESPACE;"
mysqldump -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME $TABLE_NAME > $DEST_SQL_PATH/$DB_NAME/$TABLE_NAME.sql
"""    
execu("mkdir %s"%DEST_SQL_PATH, exitOnErr = False)
for entry in result:
    print "echo 'process %s'"% entry
    execu("mkdir %s"%join(DEST_SQL_PATH, entry), exitOnErr = False)
    for name in result[entry]:
        cmd = template.replace("$MYSQL_DB_USER", MYSQL_DB_USER);
        cmd = cmd.replace("$MYSQL_DB_PASSWORD", MYSQL_DB_PASSWORD);
        cmd = cmd.replace("$RECOVER_DB_PATH", RECOVER_DB_PATH);
        cmd = cmd.replace("$DB_NAME", entry);
        cmd = cmd.replace("$TABLE_NAME", name);
        cmd = cmd.replace("$DEST_SQL_PATH", DEST_SQL_PATH);
        for runcmd in cmd.split("\n"):
            print runcmd
            if RUN:
                system(runcmd)

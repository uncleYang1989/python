#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import commands
import sys
from os.path import join
RECOVER_DB_PATH = "/jyang";
MYSQL_DB_PATH = "/var/lib/mysql"
databases = ["commsky_nms", "commsky_auth"];
result = {};
def execu(cmd, exitOnErr = True, printErrLog = True):
    print cmd
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

sqltmp = "cp -f %s.ibd %s.ibd"    
for entry in result:
    print "echo 'process %s'"% entry
    for name in result[entry]:
        cmd = sqltmp%(join(RECOVER_DB_PATH, entry, name), join(MYSQL_DB_PATH, entry, name))
        sts, text = execu(cmd)

#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import commands
import sys
from os.path import join
RECOVER_DB_PATH = "/Users/yangjie/Desktop/allinone/trouble/newdon20170113/newdonmysqlrecover";
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
    stringtmp = "hexdump -C %s.ibd |head -n 3 |tail -n 1|awk '{print $6$7}'";
    spaceIds = [];
    for name in names:
        sts, text = execu(stringtmp % join(databasePath, name))
        spaceIds.append(int(text, 16));
    result[database] = [max(spaceIds), names, spaceIds]
for entry in result:
    print entry, result[entry][0]
    

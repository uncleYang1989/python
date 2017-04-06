#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
'''
@author  yangjie
@date    2016-02-06
@desc    auto recover mysql for version 3.2.0
'''

RECOVER_DB_PATH = "/root/install/jyang/mysql"
REAL_RECOVER_DB_PATH = RECOVER_DB_PATH
DEST_SQL_PATH = "/root/install/jyang/backup";

#run recover cmd
RUN = True
#delete last backup file
DELETE_OLD = True
#forbid user choose
SLIENT = True
#enable on slent is true
AUTO_IGNORE = True

import commands
import sys
import time
from os.path import join

MYSQL_DB_USER = "root"
MYSQL_DB_PASSWORD = "c0mm3ky"
tableRelation = {"user_info":["user_role_relation"]};
ignoreTable=[]
#ignoreTable = ['client_statistics_ssid_minute', 'client_session', 'device_interface_info'];
databases = ["commsky_nms", "commsky_auth"];
CMD_DISCARD = """mysql -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME -e "ALTER TABLE $TABLE_NAME DISCARD TABLESPACE;" """
CMD_DROP = """mysql -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME -e "DROP TABLE IF EXISTS $TABLE_NAME;" """
CMD_IMPORT = """mysql -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME -e "ALTER TABLE $TABLE_NAME IMPORT TABLESPACE;" """
CMD_BACKUP = """mysqldump -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD $DB_NAME $TABLE_NAME > $DEST_SQL_PATH/$DB_NAME/$TABLE_NAME.sql"""
CMD_RECOVER = "mysql -f $DB_NAME -u$MYSQL_DB_USER -p$MYSQL_DB_PASSWORD< $DEST_SQL_PATH/$DB_NAME/$TABLE_NAME.sql"
CMD_MAIN = CMD_DISCARD + """
cp -f $RECOVER_DB_PATH/$DB_NAME/$TABLE_NAME.ibd /var/lib/mysql/$DB_NAME/
chown mysql:mysql /var/lib/mysql/$DB_NAME/*
chmod g+w /var/lib/mysql/$DB_NAME/*
""" + CMD_IMPORT + "\n" + CMD_BACKUP
processMap = {};
totalCount = 0;
successCount = 0;
faildRecord = []
STS_IGNORE = -100;
def execu(cmd, exitOnErr=True, printErrLog=True, retry=0, passTxt=""):
    print "\n\nCMD: ", cmd
    time.sleep(0.1)
    sts, txt = commands.getstatusoutput(cmd)
    if 0 == sts and txt.strip():
        print txt
    tryCount = 0;
    while True:
        if 0 == sts:
            break;
        else:
            print sts, ", ", txt
            if passTxt and -1 != txt.find(passTxt):
                print "PASS: find passtxt"
                return sts, txt
            
            if retry > tryCount:
                time.sleep(1)
                print "Retry : ", tryCount, cmd
                tryCount += 1
                sts, txt = commands.getstatusoutput(cmd)
                if 0 == sts and txt.strip():
                    print txt
            elif retry > 0 and not SLIENT and str(raw_input("\nRetry ? Y/N\n")).lower() == "y":
                    tryCount = 0
            else:
                break
    if sts != 0:
        if printErrLog:
            print "ERROR : ", sts, txt
        if exitOnErr:
            if (not SLIENT and str(raw_input("\nIgnore? Y/N\n")).lower() == "y") or (SLIENT and AUTO_IGNORE):
                print "IGNORE:", cmd
                return STS_IGNORE, ""
            onExit(sts);
    return sts, txt

def relaceKey(tmp, dbUser, dbPwd, dbPath, dbName, tableName, descSqlPath):
    cmd = tmp.replace("$MYSQL_DB_USER", dbUser);
    cmd = cmd.replace("$MYSQL_DB_PASSWORD", dbPwd);
    cmd = cmd.replace("$RECOVER_DB_PATH", dbPath);
    cmd = cmd.replace("$DB_NAME", dbName);
    cmd = cmd.replace("$TABLE_NAME", tableName);
    cmd = cmd.replace("$DEST_SQL_PATH", descSqlPath);
    return cmd;

def onExit(sts):
    msg = "Total[%d] Success[%d] Faild[%d]"%(totalCount, successCount, len(faildRecord))
    length=len(msg)
    northsouth = max(60,length*2)
    space = 10
    westeast=max((northsouth-length)/2-space, 1)
    print "\n\n"
    print "#"*northsouth
    print "#"*westeast + " "*space + msg + " "*space + "#"*westeast
    print "#"*northsouth
    if faildRecord:
        print "####################  Faild List  ##########################\n"
        print faildRecord
        print "\n############################################################"
    sys.exit(sts);
if __name__ == "__main__":
    
    # 1 collect tablenames by db name
    for database in databases:
        databasePath = join(RECOVER_DB_PATH, database);
        sts, text = execu("ls %s" % databasePath)
        names = set(text.replace("\n", " ").replace("db.opt", "").replace(r".ibd", "").replace(r".frm", "").replace("  ", " ").split(" "));
        processNames = [];
        for name in names:
            if not name.startswith("iinser"):
                processNames.append(name)
        totalCount += len(processNames);
        processMap[database] = processNames;

    # 2 clean old data
    if DELETE_OLD:
        execu("rm -rf %s" % DEST_SQL_PATH, exitOnErr=False)
    execu("mkdir %s" % DEST_SQL_PATH, exitOnErr=False)
    count = 0;
    
    
    # 3 recover table data one by one
    for dbName in processMap:
        print "process %s" % dbName
        if DELETE_OLD:
            execu("rm -rf %s" % join(DEST_SQL_PATH, dbName), exitOnErr=False)
        execu("mkdir %s" % join(DEST_SQL_PATH, dbName), exitOnErr=False)
        for name in processMap[dbName]:
            result = True
            if ignoreTable.count(name) > 0:
                print "IGNORE : " , name
                continue;
            count += 1
            print "\n\n================= ", count , "-", name, " ====================\n\n"
            recoverRelationTablesNames = [];
            if RUN and name in tableRelation:
                    relationTableNames = tableRelation[name]
                    for relationTableName in relationTableNames:
                        importcmd = relaceKey(CMD_IMPORT, MYSQL_DB_USER, MYSQL_DB_PASSWORD, REAL_RECOVER_DB_PATH, dbName, relationTableName, DEST_SQL_PATH)
                        execu(importcmd, exitOnErr=False);
                        backcmd = relaceKey(CMD_BACKUP, MYSQL_DB_USER, MYSQL_DB_PASSWORD, REAL_RECOVER_DB_PATH, dbName, relationTableName, DEST_SQL_PATH)
                        passTxt = r"doesn't exist";
                        sts, txt = execu(backcmd, retry=3, passTxt=passTxt);
                        if -1 == txt.find(passTxt):
                            recoverRelationTablesNames.append(relationTableName);
                            dropcmd = relaceKey(CMD_DROP, MYSQL_DB_USER, MYSQL_DB_PASSWORD, REAL_RECOVER_DB_PATH, dbName, relationTableName, DEST_SQL_PATH)
                            execu(dropcmd, retry=3);
            if RUN:
                time.sleep(0.5)
            cmd = relaceKey(CMD_MAIN, MYSQL_DB_USER, MYSQL_DB_PASSWORD, REAL_RECOVER_DB_PATH, dbName, name, DEST_SQL_PATH)
            for runcmd in cmd.split("\n"):
                if RUN:
                    sts, txt = execu(runcmd, exitOnErr=True, retry=3)
                    if STS_IGNORE == sts:
                        print "IGNORE:", dbName, name
                        result = False
                        break;
                else:
                    print runcmd
            if result:
                successCount += 1;
            else:
                faildRecord.append(dbName+"."+name);
            for relationTableName in recoverRelationTablesNames:
                recoverCmd = relaceKey(CMD_RECOVER, MYSQL_DB_USER, MYSQL_DB_PASSWORD, REAL_RECOVER_DB_PATH, dbName, relationTableName, DEST_SQL_PATH)
                execu(recoverCmd, retry=3);
    onExit(0);
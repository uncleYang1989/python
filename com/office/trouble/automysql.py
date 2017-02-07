#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import commands
import sys
import time
from os.path import join
RECOVER_DB_PATH = "/jyang2017/recover/var/lib/mysql"
REAL_RECOVER_DB_PATH = "/jyang2017/recover/var/lib/mysql"
DEST_SQL_PATH = "/jyang2017/backup";
MYSQL_DB_USER = "root"
MYSQL_DB_PASSWORD = "c0mm3ky"
RUN = True
DELETE_OLD = False
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

STS_IGNORE = -100;
result = {};
def execu(cmd, exitOnErr=True, printErrLog=True, retry=0, passTxt=""):
    print "\n\nCMD: ", cmd
    time.sleep(0.1)
    sts, txt = commands.getstatusoutput(cmd)
    if txt.strip():
        print txt
    tryCount = 0;
    while 0 != sts and retry > tryCount:
        if passTxt:
            if -1 != txt.find(passTxt):
                return sts, txt
        print sts, ", ", txt
        time.sleep(1)
        print "retry : ", tryCount
        print cmd
        tryCount += 1
        if tryCount >= retry:
            if str(raw_input("\nRetry ? Y/N\n")).lower() == "y":
                print "Retry:", cmd
                tryCount = 0
        sts, txt = commands.getstatusoutput(cmd)
    if sts != 0:
        if printErrLog:
            print "ERROR : ", sts, txt
        if exitOnErr:
            if str(raw_input("\nIgnore? Y/N\n")).lower() == "y":
                print "IGNORE:", cmd
                return STS_IGNORE, ""
            sys.exit(sts);
    return sts, txt

def relaceKey(tmp, dbUser, dbPwd, dbPath, dbName, tableName, descSqlPath):
    cmd = tmp.replace("$MYSQL_DB_USER", dbUser);
    cmd = cmd.replace("$MYSQL_DB_PASSWORD", dbPwd);
    cmd = cmd.replace("$RECOVER_DB_PATH", dbPath);
    cmd = cmd.replace("$DB_NAME", dbName);
    cmd = cmd.replace("$TABLE_NAME", tableName);
    cmd = cmd.replace("$DEST_SQL_PATH", descSqlPath);
    return cmd;

if __name__ == "__main__":
    # 1 collect tablenames by db name
    for database in databases:
        databasePath = join(RECOVER_DB_PATH, database);
        sts, text = execu("ls %s" % databasePath)
        names = set(text.replace("\n", " ").replace("db.opt", "").replace(r".ibd", "").replace(r".frm", "").replace("  ", " ").split(" "));
        result[database] = names;

    # 2 clean old data
    if DELETE_OLD:
        execu("rm -rf %s" % DEST_SQL_PATH, exitOnErr=False)
    execu("mkdir %s" % DEST_SQL_PATH, exitOnErr=False)
    count = 0;

    # 3 recover table data one by one
    for dbName in result:
        print "process %s" % dbName
        if DELETE_OLD:
            execu("rm -rf %s" % join(DEST_SQL_PATH, dbName), exitOnErr=False)
        execu("mkdir %s" % join(DEST_SQL_PATH, dbName), exitOnErr=False)
        for name in result[dbName]:
            if name.startswith("iinser"):
                continue;
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
                        break;
                else:
                    print runcmd
            for relationTableName in recoverRelationTablesNames:
                recoverCmd = relaceKey(CMD_RECOVER, MYSQL_DB_USER, MYSQL_DB_PASSWORD, REAL_RECOVER_DB_PATH, dbName, relationTableName, DEST_SQL_PATH)
                execu(recoverCmd, retry=3);

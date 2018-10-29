#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月13日

@author: jyang
'''
from aliyun.usermgt.usermgtUtil import *
from aliyun.usermgt import HOSTNAME, APPNAME, USERS
import json
import sys


def getDataDomainPerms(selectDomains=[], forbidDomains=[]):
    import pinyin
    perms = []
    datas = """
    杭州市全域
    十城区
    六城区
    上城大队
    下城大队
    西湖大队
    江干大队
    拱墅大队
    滨江大队
    下沙大队
    高架大队
    绕城大队
    景区大队
    大江东大队
    萧山大队
    余杭大队
    富阳大队
    临安大队
    桐庐大队
    淳安大队
    建德大队
    """.strip().split("\n")
    for data in datas:
        if selectDomains:
            if data not in selectDomains:
                continue;
        elif forbidDomains:
            if data in forbidDomains:
                continue;
        perms.append("domain:" + pinyin.get(data, format="numerical").strip())
    return perms


def getUiPerms(forbidApps=[], forbidUIs=[]):
    perms = []
    data = {
        "datav":["hover:r", "main:r"],
        "upps":["page:home",
                "page:manual",
                "op:msg:edit",
                "page:home          " ,
                "page:manual        " ,
                "op:msg:edit        " ,
                "op:msg:examine     " ,
                "page:auto          " ,
                "page:media         " ,
                "op:suggest:reply   " ,
                "page:setting       " ,
                "page:statistics    " ,
                "page:info-type     " ,
                "page:si            " ,
                "page:author        " ,
                "page:bcsetting     " ,
                "page:log           " ,
                "page:parameter     " ,
                "page:escort        " , ],
        "event_handle":[
                "op:home:message   ",
                "page:area         ",
                "page:settings     ",
                "page:handle       ",
                "page:query        ",
                "page:statis       ",
                "op:home:handle    ",
                ],
        "vehicles":[
                "page:realtime        ",
                "page:evt     ",
                "page:analyse       ",
                "page:config        "
                ],
        };
    for key in data.keys():
        if key in forbidApps:
            continue;
        perms.append("ui:" + key)
        controls = data[key];
        for control in controls:
            if control.strip() in forbidUIs:
                continue
            perms.append("ui:" + key + ":" + control.strip());
    return perms


def createModel(hostname, appName, username, rid, password="admin", forbidApps=[], forbidUIs=[], selectDomains=[], forbidDomains=[]):
    
    print "createUser", createUser(hostname, appName, username, password)
    print "assinRole", assinRole(hostname, appName, username, rid);
    
    perms = [];
    perms.extend(getDataDomainPerms(selectDomains, forbidDomains))
    perms.extend(getUiPerms(forbidApps, forbidUIs))
    
    for perm in perms:
        print assignPerm(hostname, appName, perm, rid);

def createRoles(roleName):
    resRole = createRole(HOSTNAME, APPNAME, roleName);
#     resRole = """
#     {"code":"SUCCESS","data":{"id":18,"app_name":"__base__","name":"testRole","desc":null,"status":null,"gmt_created":"2018-07-27 11:01:11","is_deleted":0,"gmt_modified":"2018-07-27 11:01:11"}}
# """
    roleInfo = json.loads(resRole);
    if roleInfo["code"] == "SUCCESS":
        return roleInfo["data"]["id"];
    else:
        sys.exit(1);


if __name__ == '__main__':
    hostname = HOSTNAME
    appName = APPNAME

    users = []
    users.append("a7");
    for user in users:
        print "create user ", user
        rid = createRoles(user)
        createModel(hostname, appName, user, rid, forbidApps=["event_handle"])
#     createModel(hostname, appName)
    

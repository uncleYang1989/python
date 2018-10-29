#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月13日

@author: jyang
'''
from aliyun.usermgt.usermgtUtil import *
from aliyun.usermgt import HOSTNAME, APPNAME, USERS
from aliyun.usermgt.dep.createDefaultPerms import *

def createModel(hostname, appName):
    
    users = USERS;
    for user in users:
        print createUser(hostname, appName, user[0], user[1])
        print assinRole(hostname, appName, user[0], user[2]);
    
    perms = [];
    perms.extend(domainperms())
    perms.extend(getUiPerms())
    
    for perm in perms:
        print createPermit(hostname, appName, perm[1], code=perm[1],desc=perm[2]);
        print assignPerm(hostname, appName, perm[1], users[0][2]);
        
        if perm[1].startswith("domain:"):
            if perm[1] == "domain:shang4cheng2da4dui4":
                    print assignPerm(hostname, appName, perm[1], users[1][2]);
                    print assignPerm(hostname, appName, perm[1], users[2][2]);
        else:
            if perm[1] not in ["ui:upps:page:manual", "ui:event_handle:page:statis", "ui:vehicles:page:realtime"]:
                print assignPerm(hostname, appName, perm[1], users[2][2]);
            if perm[1] not in ["ui:sys_operation","ui:data_monitor"]:
                print assignPerm(hostname, appName, perm[1], users[1][2]);


if __name__ == '__main__':
    hostname = HOSTNAME
    appName = APPNAME
    createModel(hostname, appName)
    

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
    
#     users = USERS;
#     for user in users:
#         print createUser(hostname, appName, user[0], user[1])
#         print assinRole(hostname, appName, user[0], user[2]);
#     
    perms = [];
    perms.extend(domainperms())
    perms.extend(getUiPerms())
    print len(perms)
    for permTmp in perms:
        print permTmp[0].encode('utf-8')
#         print createPermit(hostname, appName, permTmp[0].encode('utf-8'), code=permTmp[1],desc=permTmp[2]);
#         
#         print assignPerm(hostname, appName, permTmp[0].encode('utf-8'), USERS[0][2]);
# #         
#         if permTmp[1].startswith("domain:"):
#             if permTmp[1] == "domain:shang4cheng2da4dui4":
#                     print assignPerm(hostname, appName, permTmp[0].encode('utf-8'), USERS[1][2]);
#                     print assignPerm(hostname, appName, permTmp[0].encode('utf-8'), USERS[2][2]);
#         else:
#             if permTmp[1] not in ["ui:upps:page:manual", "ui:event_handle:page:statis", "ui:vehicles:page:realtime"]:
#                 print assignPerm(hostname, appName, permTmp[0].encode('utf-8'), USERS[2][2]);
#             if permTmp[1] not in ["ui:sys_operation","ui:data_monitor"]:
#                 print assignPerm(hostname, appName, permTmp[0].encode('utf-8'), USERS[1][2]);


if __name__ == '__main__':
    hostname = HOSTNAME
    appName = APPNAME
    createModel(hostname, appName)
    

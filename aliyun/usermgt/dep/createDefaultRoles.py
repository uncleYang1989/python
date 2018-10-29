#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月13日

@author: jyang
'''
from aliyun.usermgt.usermgtUtil import createRole, assignPerm
from aliyun.usermgt import HOSTNAME, APPNAME
from aliyun.usermgt.dep.src import *

def todo(roleName, roleMap, perms, rawRoleName):
    import json
    print "roleName",roleName
    if type(perms) != list:
        perms = [perms];
    print "perms", 
    for perm in perms:
        print perm,
    print
    roleName = roleName.encode("utf-8")
#     tmp = u"""
#     {"code":"SUCCESS",u"data":{"id":5,u"app_name":"__base__",u"name":"test",u"desc":null,u"status":null,u"gmt_created":"2018-08-05 15:05:44",u"is_deleted":0,u"gmt_modified":"2018-08-05 15:05:44"}}
# """
    tmp = createRole(HOSTNAME, APPNAME, roleName, 1, 1)
    resObj = json.loads(tmp);
    if resObj["code"] == "SUCCESS":
        data = resObj["data"]
        roleMap[rawRoleName] = data;
        for perm in perms:
            print "add", perm , "to", roleName
            print assignPerm(HOSTNAME, APPNAME, perm.encode("utf-8"), data["id"])
    else:
        print tmp



def domainpermsByPerms(perms, domainPerms):
    resultPerms = [];
    appPermKeys = [u"evt",u"ver",u"upps"]
    curAppPermKeys = []
    for appPermKey in appPermKeys:
        for perm in perms:
            if perm.count(appPermKey):
                curAppPermKeys.append(appPermKey)
                break
    for domainPerm in domainPerms:
        dataVdomain = 1;
        for appPermKey in appPermKeys:
            if domainPerm.count(appPermKey):
                dataVdomain -= 1
        if dataVdomain:
            resultPerms.append(domainPerm)
        else:
            for appPermKey in curAppPermKeys:
                if domainPerm.count(appPermKey):
                    resultPerms.append(domainPerm)
                    break
    return resultPerms
                
def domainpermsByPermsRoleName(roleName, domainPerms):
    resultPerms = [];   
    for domainPerm in domainPerms:
        if domainPerm.count(roleName[:2]):
            resultPerms.append(domainPerm)
    return resultPerms
            
def importRoles():
    roleMap = {};
    allDomainPerms = rolesPerm[u"全域数据管理角色"].strip().split("\n")
    
    for roleName in rolesPerm.keys():
        todo(roleName, roleMap, rolesPerm[roleName].strip().split("\n"), roleName)
    
    for defaultEmptyRole in defaultEmptyRoles.strip().split("\n"):
        perms = []
        if defauleRolePermLimit.has_key(defaultEmptyRole):
            perms = defauleRolePermLimit[defaultEmptyRole].strip().split("\n")
            perms.extend(domainpermsByPerms(perms, allDomainPerms))
        elif defaultEmptyRole.endswith(u"大队"):
            perms = daduiRole.strip().split("\n")
            perms.extend(domainpermsByPermsRoleName(defaultEmptyRole, allDomainPerms))
        else:
            print defaultEmptyRole, "没有权限"
        perms.append(u"权限管理登录")
        perms.append(u"权限管理-页面-角色管理")
        perms.append(u"权限管理-页面-用户管理")
        
        todo(defaultEmptyRole + u'管理员角色', roleMap, perms, defaultEmptyRole)
    return roleMap;
if __name__ == "__main__":

    ids = """
1
3
5
9
12
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
35
42
44
45
59
60
62
63
67
68
69
71
72
77
78
79
80
81
82
83
84
85
86
87
88
89
91
92
93
94
95
96
97
110
113
114
115
116
117
118
119
120
121
127
""".strip().split("\n");
    print ids
    for id in ids:
        print assignPerm(HOSTNAME, APPNAME, u"公众服务-页面-统计分析".encode("utf-8"), id)
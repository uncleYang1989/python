#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月13日

@author: jyang
'''
from aliyun.util.httpUtil import get, post
def login(HOSTNAME, APPNAME, username, password):
    url = HOSTNAME + "/user/login"
    textmod = {"username": username, "password": password, "app_name": APPNAME}
    return post(url, textmod)
    
def createUser(HOSTNAME, APPNAME, username, password, orgName = "网络管理员", nickname="", nid=0, sort_type = 999999999):
    url = HOSTNAME + "/user/add"
    textmod = {"user":{"username": username, "password": password, "app_name": APPNAME, "nickname":nickname, "nid":nid, "sort_type":sort_type}}
    if orgName:
        textmod["user"]["payload"]='{"organization":"%s"}'%orgName
    return post(url, textmod)

def getUserInfo(HOSTNAME, APPNAME, username):
    url = HOSTNAME + "/user/getById"
    textmod = {"username": username, "app_name":APPNAME}
    return get(url, textmod)

def assinRole(HOSTNAME, APPNAME, username, rid, init = None):
    url = HOSTNAME + "/user/assignRole"
    textmod = {"username": username, "rid":rid, "app_name": APPNAME}
    if init:
        textmod["init"] = 1
    return post(url, textmod)

def assinRoleBatch(HOSTNAME, APPNAME, username, rid):
    url = HOSTNAME + "/user/assignRoleBatch"
    textmod = {"username": username, "rid":rid, "app_name": APPNAME}
    return post(url, textmod)
def cleanRoleBatch(HOSTNAME, APPNAME, username):
    url = HOSTNAME + "/user/cleanRole"
    textmod = {"username": username, "app_name": APPNAME}
    return post(url, textmod)

def createRole(HOSTNAME, APPNAME, roleName,is_managent,create_uid):
    url = HOSTNAME + "/role/create"
    textmod = {"role":{"app_name":APPNAME, "name":roleName, "create_uid":create_uid, "is_managent":is_managent}}
    return post(url, textmod)

def assignPerm(HOSTNAME, APPNAME, permitName, rid):
    url = HOSTNAME + "/role/assignPerm"
    textmod = {u"app_name":APPNAME, u"pname":permitName, u"rid" : rid}
    return get(url, textmod)

def createPermit(HOSTNAME, APPNAME, permitName, code="", desc=""):
    url = HOSTNAME + "/perms/create"
    if not code:
        code = permitName;
#     textmod = {"perm":{"app_name":APPNAME, "name":code, "desc" : desc}}
    textmod = {"perm":{"app_name":APPNAME, "name":permitName, "code":code, "desc" : desc}}
    return post(url, textmod)

def deletePermit(HOSTNAME, permitId):
    url = HOSTNAME + "/perms/delete"
    textmod = {"ids":permitId}
    return get(url, textmod)

def listPermit(HOSTNAME, APPNAME):
    url = HOSTNAME + "/perms/listAll"
    textmod = {"app_name":APPNAME,"qs":"","pageNum":0,"pageSize":1000}
    print APPNAME
    return get(url, textmod)

def changePermit(HOSTNAME, APPNAME, pid, name, desc):
    url = HOSTNAME + "/perms/change"
    textmod = {"perm":{"app_name":APPNAME, "id":pid,"name":name,"desc":desc}}
    return post(url, textmod)

def createOrg(HOSTNAME, APPNAME, name, code, owner = "", desc = "",rid = ""):
    url = HOSTNAME + "/orgTree/create"
    textmod = {"rid":rid, "node":{"app_name":APPNAME, "code":code,"name":name,"desc":desc, "owner":owner}}
    return post(url, textmod)

def getOrg(HOSTNAME, APPNAME, code):
    url = HOSTNAME + "/orgTree/getNodeInfo"
    textmod = {"app_name":APPNAME,"code":code}
    return get(url, textmod)

def bindOrgUser(HOSTNAME, uid, nid):
    url = HOSTNAME + "/orgTree/bindUser"
    textmod = {"uid":uid,"nid":nid}
    return post(url, textmod)

def listTree(HOSTNAME, rid, parse = None):
    url = HOSTNAME + "/orgTree/listTree"
    textmod = {"rid":rid}
    if parse:
        textmod["parse"] = 1
    return get(url, textmod)

def listPermById(HOSTNAME, APPNAME, uid):
    url = HOSTNAME + "/perms/listAllByUid"
    textmod = {"uid":uid, "app_name":APPNAME}
    return get(url, textmod)

def changPwd(HOSTNAME, username, lastPassword, password):
    url = HOSTNAME + "/user/modpwd"
    textmod = {"username":username,"last_password":lastPassword, "password":password}
    return post(url, textmod)


if __name__ == '__main__':
    from aliyun.usermgt import *
#     print listPermit(HOSTNAME, "__base__")
#     print createOrg(HOSTNAME, APPNAME, "tt", "tt")
#     print getOrg(HOSTNAME, APPNAME, "tt")
#     print assinRoleBatch(HOSTNAME, APPNAME, ["110734","011249","011075"], [4])
#     print cleanRoleBatch(HOSTNAME, APPNAME, ["011244","011288"])
#     print bindOrgUser(HOSTNAME, 1, 1)#todo
#     print createRole(HOSTNAME, APPNAME, "444444444444444", 1, 1);
    print changPwd(HOSTNAME, "admin", "admin1", "admin")
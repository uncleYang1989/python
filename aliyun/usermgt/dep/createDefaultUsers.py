#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月30日

@author: jyang
'''
from aliyun.util.excelUtil import read
from aliyun.usermgt import *
from aliyun.usermgt.usermgtUtil import *
from usersrc import *
from src import *
from aliyun.usermgt.dep.src import defaultEmptyRoles
GW_MAP = {
     'A':[u'中队长',800],
     'B':[u'副中队长',900],
     'C':[u'教导员', 210],
     'D':[u'大队长', 200],
     'E':[u'副大队长', 300],
     'F':[u'指导员', 850],
     'G':[u'普通民警', 1000],
     'H':[u'支队领导', 10],
     'I':[u'处长', 200],
     'J':[u'副处长', 300],
     'M':[u'内勤', 950],
     'L':[u'未知', 1100],
    }
LINGDAO_INDEX = \
[
    u"金洪亮",
    u"王叶飞",
    u"徐逸峰",
    u"郑建国",
    u"方国尧",
    u"闫春雷",
    u"孔万锋",
    u"俞小平",
    u"孟涛",
    u"来坚农",
    u"陆宝根",
    ]
ingoreLingDaoJH = [
    "010037",
    "011000",
    "010997",
    "011011",
    "010122",
    "011179",
    "010281",
    "013001",
    "011903",
    "011071"
    ]
import json

# validCodes = ['330182005700', '330106000000', '330100000803', '330102005500', '330105005500', '330182000000', '330103005300', '330127005300', '330199005200', '330198000300', '330185001500', '330100000800', '330182005400', '330100001100', '330106000404', '330106000407', '330100000702', '330110005500', '330105000300', '330100000700', '330100000701', '330110001500', '330183001500', '330193000000', '330195000000', '330183005300', '330198005200', '330110005400', '330150005300', '330197000000', '330199000000', '330102000401', '330109006000', '330183005400', '330109000400', '330108005100', '330102000402', '330185005500', '330122000100', '\\N', '330102000405', '330199005100', '330122001400', '330104005400', '330127000000', '330199005500', '330102005200', '330103000300', '330186000000', '330195005100', '330104005200', '330100000403', '330100000402', '330100000401', '330100000400', '330100000407', '330106005700', '330100000405', '330100000404', '330110005700', '330189000400', '330100000408', '330183006100', '330183000400', '330183000401', '330110005300', '330182005600', '330105000000', '330193005700', '330199005400', '330102000404', '330185005800', '330102005400', '330103005400', '330122000700', '330122000701', '330110005800', '330109000000', '330185001200', '330182005200', '330108000000', '330105000406', '330105005200', '330100000000', '330197005400', '330196005200', '330100000406', '330193006100', '330193006800', '330106005800', '330105000405', '330183000000', '330100001301', '330105000408', '330197005300', '330104000300', '330105000407', '330100001300', '330105000402', '330105000403', '330183005500', '330100000301', '330122005100', '330185000000', '330182005500', '330110000800', '330109005300', '330127005700', '330100000901', '330106005200', '330105000401', '330109005100', '330102000403', '330182005300', '330186002200', '330199005600', '330182001100', '330108000300', '330193005100', '330127000300', '330110000300', '330193005300', '330109005900', '330105005600', '330186002300', '330100000902', '330100001204', '330103005000', '330106005600', '330106005000', '330102000300', '330100001201', '330185005300', '330109005600', '330102000000', '330199005000', '330122000400', '330183000300', '330104000000', '330182005100', '330196000300', '330127005100', '330122005300', '330100001205', '330127001500', '330108005200', '330193006300', '330150005100', '330122000000', '330193005000', '330110000100', '330104005500', '330109005500', '330100000107', '330105005300', '330100000105', '330100000102', '330100000103', '330100000100', '330100000101', '330193006400', '330106005900', '330185005700', '330109005200', '330186002100', '330197005200', '330110005600', '330104000407', '330104000405', '330150000000', '330183005600', '330102005000', '330122005000', '330185000300', '330106000300', '330127005400', '330104000409', '330100001501', '330100001500', '330100001503', '330100001502', '330122000300', '330100001504', '330102000406', '330150000300', '330104005300', '330196000000', '330195000300', '330197000300', '330100000903', '330110001200', '330100001401', '330122005400', '330110000600', '330108000403', '330105005400', '330182000300', '330103005200', '330109005700', '330127005200', '330199005300', '330100000900', '330193006600', '330185000400', '330110000400', '330193005200', '330193005600', '330100000601', '330127005800', '330100000603', '330100000602', '330103005500', '330182001500', '330122005200', '330198000000', '330100000802', '330100000801', '330127005600', '330109001100', '330183005200', '330198005100', '330150005200', '330127001200', '330185005600', '330110000000', '330100000600', '330182000400', '330104005600', '330100000300', '330185005400', '330100000302', '330100000303', '330196005100', '330103000409', '330108005300', '330197005100', '330103000401', '330103000402', '330103000403', '330103000404', '330102005300', '330103000406', '330103000407', '330105005000', '330186000300', '330185005200', '330127005500', '330127000400', '330100001400', '330100001202', '330100001402', '330100001403', '330100001404', '330100001405', '330106005400', '330183001200', '330109001500', '330100001200', '330104005000', '330103000000', '330109000100'];
def installUser(orgMap):
    orgCodeList = orgcodes.strip().split("\n")
    userTables = read(r"/Users/jyang/Desktop/警员信息080823.xlsx", u"工作表1")
    unknownGw = []
    unknownCode = []
    validCodes = []
    count = 0
    for row in userTables[1:]:
#         print row
#         continue
        jid = row[1]
        name = row[4]
        gw = row[3]
        code = orgCodeList[count];
        count += 1
        password = "123456"
        if len("330104005300") != len(code):
            pass
        else:
            username = str(jid).replace(".0", "").rjust(6,"0").upper()
            nickname = name
            orgName = u"岗位[%s]"%gw
            if username in ingoreLingDaoJH:
#                 print u"忽略过期的警号", username
                continue
            try:
                int(username);
            except:
#                 print u"忽略非数字的警号", username
                continue
            
            if GW_MAP.has_key(gw):
                orgName = GW_MAP[gw][0]
            else:
                #TPDP
                unknownGw.append(gw)
                continue;
#             print username, nickname, orgName, code

            orgInfo = [0, ""]
            if not orgMap.has_key(code):
                unknownCode.append(code)
                code = code[:6].ljust(12, "0")
                if not orgMap.has_key(code):
#                     print "noid"
                    continue;
                orgInfo = orgMap[code]
            else:
                orgInfo = orgMap[code]
            
            if orgInfo[0]:
                if orgInfo[1].endswith(u"所"):
                    orgName = orgName.replace(u"中队长", u"所长");
                elif orgInfo[1].endswith(u"科"):
                    orgName = orgName.replace(u"中队长", u"科长");
                sortType = GW_MAP[gw][1]
                try:
                    sortType = sortType + LINGDAO_INDEX.index(nickname);
                    print nickname
                except:
                    pass
                print assinRole(HOSTNAME, APPNAME, username, 37);
#                 print createUser(HOSTNAME, APPNAME, username, password, orgName, nickname, orgInfo[0], sortType)
                validCodes.append(code)
#                 import time
#                 time.sleep(0.001)
#     print set(unknownGw)
#     print set(unknownCode)
#     print set(validCodes)
#     print len( set(validCodes));
    
#     print set(orgCodeList)
#     print len( set(orgCodeList));
def initOrgMap():
    res = listTree(HOSTNAME, 1)
    resObj = json.loads(res);
    orgList = resObj["data"]
    orgMap = {}
    for org in orgList:
        orgMap[org["code"]] = [org["id"], org["name"]]
    return orgMap

def createSimpleUser():
    for user in USERS:
        print createUser(HOSTNAME, APPNAME, user[0], user[1])
        print getUserInfo(HOSTNAME, APPNAME, user[0]);
        print assinRole(HOSTNAME, APPNAME, user[0], user[2]);
    print bindOrgUser(HOSTNAME, 1, 1)

def parseToUserName(roles):
    import pinyin
    usernames = [];
    for role in roles.strip().split("\n"):
        tmpName = "";
        for code in role.strip():
            if code.count(u"萧"):
                tmpName += u"xiao";
            else:
                tmpName += pinyin.get(code, format="numerical").strip()[0];
        usernames.append([role, tmpName + "admin"])
    return usernames

def installDefaultUser(roles, roleMap, roleCodeRelation, orgMap):
    usernames = parseToUserName(roles);
    password = "123456"
    for roleName, username in usernames:
        print roleName, username, password
        continue
        if roleMap.has_key(roleName):
            roleDict = roleMap[roleName]
            rid = roleDict["id"]
            code = roleCodeRelation[roleName];
            print createUser(HOSTNAME, APPNAME, username, password, "网络管理员", roleName, orgMap[code][0])
            print getUserInfo(HOSTNAME, APPNAME, username);
            print assinRole(HOSTNAME, APPNAME, username, rid);

def importUser(roleMap):    
#     createSimpleUser()
    orgMap = initOrgMap();
#     installUser(orgMap)
#     installDefaultUser(defaultEmptyRoles, roleMap, roleCodeRelation, orgMap);
    

if __name__ == "__main__":
    importUser(None)

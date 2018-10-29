#!/usr/bin/python
# encoding=utf8
'''
Created on 2018年7月13日

@author: jyang
'''
from aliyun.usermgt.usermgtUtil import login
from aliyun.usermgt import HOSTNAME, APPNAME
import sqlite3, time, threading
def doByTimeout(callable__, arg, timeoutNum=60):
    print arg
    '''
    允许设置超时时间的处理函数
    '''
    t = threading.Thread(target=callable__, args=(arg,))
    t.start()
#     success = False
#     timeoutNum = timeoutNum * 100;
#     while timeoutNum > 0:
#         if t.isAlive():
#             timeoutNum -= 1;
#             time.sleep(0.01);
#         else:
#             success = True
#             break;
#     return success; 
def test(i):
    count = 0
    for i in range(100):
        count +=1;
        print i, login(HOSTNAME, APPNAME, "mifan", "admin");
    print time.time();
if __name__ == '__main__':
    print time.time();
    for i in range(10):
        doByTimeout(test, i);
#     print login(HOSTNAME, APPNAME, "usershangcheng", "admin");
#     print login(HOSTNAME, APPNAME, "usershangchengpart", "admin");
    

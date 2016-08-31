#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月8日

@author: Administrator
'''
import sys
from com.office.util.fileUtil import appendFile, getKeyList
reload(sys)
sys.setdefaultencoding('utf8')

myLost=getKeyList(r"/Users/yangjie/Downloads/1370-2215.xlsx", True, "Sheet1")
tcmidHerb=getKeyList(r"/Users/yangjie/Downloads/herb.xlsx", True, "Sheet1")
newHerb=r"/Users/yangjie/Downloads/herb.csv"
lastline0=[]
for line in myLost:
    print"handling", line
    try:
        for herbLine in tcmidHerb:
            if line[0]==herbLine[0]:
                appendFile(newHerb,herbLine[0].replace(",","，")+",")
                appendFile(newHerb,herbLine[1].replace(",","，").decode("utf8").encode("gbk")+",")
                appendFile(newHerb,"TCMID"+"\n")
        if line[0]:
            lastline0=line[0]
            appendFile(newHerb, lastline0.replace(",","，")+",")
            appendFile(newHerb, line[1].replace(",","，").decode("utf8").encode("gbk")+",")
            appendFile(newHerb, line[2].replace(",","，").decode("utf8").encode("gbk")+"\n")
        else:
            appendFile(newHerb, lastline0.replace(",","，")+",")
            appendFile(newHerb, line[1].replace(",","，").decode("utf8").encode("gbk")+",")
            appendFile(newHerb, line[2].replace(",","，").decode("utf8").encode("gbk")+"\n")
            
    except Exception,e:
        print e
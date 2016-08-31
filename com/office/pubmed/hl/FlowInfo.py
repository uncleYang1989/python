#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年5月4日
@author: huanglin
'''
from com.office.util.fileUtil import getKeyList
from com.office.util.excelUtil import read
import os

class FlowInfo():
    def __init__(self,pathname):
        import ConfigParser
        cf=ConfigParser.ConfigParser()
        cf.read(pathname)
        self.srcKeyPathname=cf.get("baseconf","srcKeyPathname");
        self.recordPathname=cf.get("baseconf","recordPathname");
        self.resultPathname=cf.get("baseconf","resultPathname");
        self.driverPathname=cf.get("baseconf","driverPathname");
#        self.keynames=cf.get("baseconf","keynames")
        
        if os.path.exists(self.recordPathname):
            self.recorddata=read(self.recordPathname)
        else:    
            self.recorddata=[]
        if os.path.exists(self.resultPathname):
            self.result=read(self.resultPathname)
        else:
            self.result=[]
        self.srcKeys=read(self.srcKeyPathname)        

if __name__ == "__main__":
    fi = FlowInfo("flowinfo.ini");
    print fi.recordPathname
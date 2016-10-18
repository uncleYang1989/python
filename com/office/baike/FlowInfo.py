#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年5月25日

@author: yangjie
'''
from com.office.util.fileUtil import getKeyList, readFile

class FlowInfo():
    def __init__(self, pathname):
        import ConfigParser
        cf = ConfigParser.ConfigParser()  
        cf.read(pathname)
        self.srcKeyPathname = cf.get("baseconf", "srcKeyPathname");
        self.recordPathname = cf.get("baseconf", "recordPathname");
        self.resultPathname = cf.get("baseconf", "resultPathname");
        
        self.keys = getKeyList(self.srcKeyPathname)
        self.keyStr = ""
        try:
            self.keyStr = readFile(self.recordPathname)
            self.keyStr = self.keyStr.decode('gbk').encode("utf8")
        except:
            pass
        # #使用第三方库，模拟浏览器登录
        from selenium import webdriver
        executable_path= "/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver"
        self.driver = webdriver.Chrome(executable_path)

if __name__ == "__main__":
    fi = FlowInfo("baike.ini");
    print fi.recordPathname
        
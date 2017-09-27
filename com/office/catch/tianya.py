#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
forbidCodeErr()
# #使用第三方库，模拟浏览器登录
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://bbs.tianya.cn/post-feeling-4285505-1.shtml");
output = ""
f = open(u"/Users/yangjie/Desktop/33.txt", "wb")
while True:
    altItemEles = driver.find_elements_by_class_name("atl-item");
    for altItemEle in altItemEles:
        _hostid = altItemEle.get_attribute("_hostid")
        if _hostid == "124716888":
            contentPart = altItemEle.find_element_by_class_name("bbs-content").text
            print "contentPart", contentPart
            output = "\n"
            output += "\n"
            output += contentPart
            output += "\n"
            f.write(output);
            f.flush();
    try:
        driver.find_element_by_class_name("js-keyboard-next").click();
    except:
        break;
driver.quit()
f.close();
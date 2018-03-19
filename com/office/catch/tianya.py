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
driver = webdriver.Chrome(executable_path="/Users/yangjie/mywork/icode/cloudnms/sky-auto/autouitest/driver/chrome/chromedriver_mac32/chromedriver")
urltmp = "http://bbs.tianya.cn/post-16-1692673-%s.shtml"

output = ""
f = open(u"/Users/yangjie/Desktop/无意间加入了神仙微信群，生活就此浪得不行了.txt", "wb")
count = 1;
lastUrl = "";
while True:
    try:
        driver.get(urltmp%count);
        if driver.current_url == lastUrl:
            break;
        else:
            count += 1
            lastUrl = driver.current_url
    except:
        continue;
    altItemEles = driver.find_elements_by_class_name("atl-item");
    for altItemEle in altItemEles:
        _hostid = altItemEle.get_attribute("_hostid")
        if _hostid == "131041227":
            contentPart = altItemEle.find_element_by_class_name("bbs-content").text
            print "contentPart", contentPart
            output = "\n"
            output += "\n"
            output += contentPart
            output += "\n"
            f.write(output);
            f.flush();
driver.quit()
f.close();
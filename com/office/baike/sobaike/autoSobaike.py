#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
from com.office.baike.FlowInfo import FlowInfo
from selenium.webdriver.common.keys import Keys
forbidCodeErr()

from com.office.util.fileUtil import appendFile
fi = FlowInfo("sobaike.ini")
#访问网站
fi.driver.get("http://baike.so.com/")
for key in fi.keys:
    print key
    if key in fi.keyStr:
        print key, "之前处理过了，这次直接跳过"
        continue
    try:
        fi.driver.find_element_by_id("J-search-word").clear();
        fi.driver.find_element_by_id("J-search-word").send_keys(key);
        fi.driver.find_element_by_id("J-mod-gosearch").click();
        fi.driver.find_element_by_id("J-mod-gosearch").send_keys(Keys.ENTER);
        h3Eles = fi.driver.find_elements_by_class_name("h3");
        for h3Ele in h3Eles:
            print h3Ele.text
        try:
            mainContentEle = fi.driver.find_element_by_id("js-card-content")
            appendFile(fi.resultPathname, (key + "," + mainContentEle.text.replace(",","，").replace("\n",";")).decode('utf8').encode("gbk") + "\n")
        except:
            appendFile(fi.resultPathname, (key + "," + "数据不存在").decode('utf8').encode("gbk") + "\n")
        #记录已经执行的关键字
        appendFile(fi.recordPathname, key.decode('utf8').encode("gbk") + "\n")
    except Exception,e:
        print e
    #记录已经执行的关键字
fi.driver.quit()

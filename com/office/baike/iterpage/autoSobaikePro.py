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
from selenium.common.exceptions import NoSuchWindowException
forbidCodeErr()

from com.office.util.fileUtil import appendFile
fi = FlowInfo("sobaike.ini")
#访问网站
fi.driver.get("http://baike.so.com/")
try:
    print "网络异常", fi.driver.find_element_by_id("main-message").text
except:
    pass
key = u"麻黄汤"
try:
    fi.driver.find_element_by_id("J-search-word").clear();
    fi.driver.find_element_by_id("J-search-word").send_keys(key);
    fi.driver.find_element_by_id("J-mod-gosearch").click();
    fi.driver.find_element_by_id("J-mod-gosearch").send_keys(Keys.ENTER);
    while True:
        try:
            nextEle = fi.driver.find_element_by_class_name("next")
#                 nextEle = fi.driver.find_element_by_xpath("//div[@id='page']/a[@class='next']")
            nextEle.send_keys(Keys.ENTER);
            print "下一页"
        except Exception, e:
            print e
            if "Unable to locate element" in e.msg:
                print "已到尾页"
                break
            elif "target window already closed" in e.msg:
                from selenium import webdriver
                executable_path="/Users/yangjie/Documents/env/jyang-site-packages/chromedriver_2.21/chromedriver_mac32/chromedriver"
                fi.driver = webdriver.Chrome(executable_path)
                fi.driver.get("http://baike.so.com/")
                
                fi.driver.find_element_by_id("J-search-word").clear();
                fi.driver.find_element_by_id("J-search-word").send_keys(key);
                fi.driver.find_element_by_id("J-mod-gosearch").click();
                fi.driver.find_element_by_id("J-mod-gosearch").send_keys(Keys.ENTER);
                print "浏览器异常关闭，重新启动"
    #记录已经执行的关键字
    appendFile(fi.recordPathname, key.decode('utf8').encode("gbk") + "\n")
except Exception,e:
    print e
#记录已经执行的关键字
# fi.driver.quit()

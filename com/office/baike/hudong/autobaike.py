#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
import time
from com.office.util.codeUtil import forbidCodeErr
from com.office.baike.FlowInfo import FlowInfo
from selenium.webdriver.common.keys import Keys
forbidCodeErr()

from com.office.util.fileUtil import appendFile
fi = FlowInfo("../baike.ini")
fi.driver.get("http://www.pubmed.com/")
# for key in fi.keys:
#     print key
#     if key in fi.keyStr:
#         print key, "之前处理过了，这次直接跳过"
#         continue
    try:
        
        fi.driver.find_elements_by_xpath("//dd/a");
        fi.driver.find_element_by_name("q").clear();
        fi.driver.find_element_by_name("q").send_keys(key);
        fi.driver.find_element_by_class_name("search-button").click();
        h3Tags = fi.driver.find_elements_by_tag_name("h3")
        matchKey = key + "_百科词条"
        for h3Tag in h3Tags:
            if h3Tag.text == matchKey:
                href = h3Tag.find_element_by_tag_name("a").get_attribute("href");
                print "findLink", href
                h3Tag.find_element_by_tag_name("a").send_keys(Keys.ENTER);
                
                '''获得当前所有的Tab页对象'''
                window_handles = fi.driver.window_handles
                print len(window_handles)
                '''切换到最后一个Tab页'''
                fi.driver.switch_to_window(window_handles[-1])
                '''搜集tab页里的内容'''
                print fi.driver.find_element_by_id("unifyprompt").text
                '''关闭tab页'''
                fi.driver.close();
                '''切换回原来的Tab页'''
                fi.driver.switch_to_window(window_handles[0])
#                 if len(window_handles) > 5:
#                     fi.driver.quit()
#                     # #使用第三方库，模拟浏览器登录
#                     from selenium import webdriver
#                     executable_path="/Users/yangjie/Documents/env/jyang-site-packages/chromedriver_2.21/chromedriver_mac32/chromedriver"
#                     fi.driver = webdriver.Chrome(executable_path)
#                     fi.driver.get("http://www.baike.com/")
#         #记录已经执行的关键字
        appendFile(fi.recordPathname, key.decode('utf8').encode("gbk") + "\n")
    except Exception,e:
        print e
    #记录已经执行的关键字
fi.driver.quit()

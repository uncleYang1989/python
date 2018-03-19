#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
from selenium import webdriver  
executable_path = "/Users/yangjie/mywork/icode/cloudnms/sky-auto/autouitest/driver/chrome/chromedriver_mac32/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path) 
running = True
while running:
    import time
    time.sleep(1) 
    driver.get("http://www.baidu.com")
    eles = driver.find_elements_by_xpath("//a[@class='text']")
    for ele in eles:
        if u"杭州市小客车增量指标竞价情况" in ele.text:
    #         print ele.text;
    #         print ele.get_attribute("href")
            pass
        elif u"2018年02月杭州市小客车增量指标摇号结果公告" in ele.text:
            print ""
            urls = ele.get_attribute("href");
            driver = webdriver.Chrome(executable_path=executable_path) 
            driver.get(urls); 
            ele = driver.find_element_by_xpath("//a[@attachid]")
            driver.get(ele.get_attribute("href"))
            running = False
            break

#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
from selenium import webdriver  
driver = webdriver.Firefox(executable_path="/Users/yangjie/Downloads/chrome/geckodriver") 
running = True
while running:
    import time
    time.sleep(1) 
    driver.get("http://xkctk.hzcb.gov.cn/tzgg/index.html")
    eles = driver.find_elements_by_xpath("//a[@class='text']")
    driver.save_screenshot("aa.png")
    for ele in eles:
        if u"杭州市小客车增量指标竞价情况" in ele.text:
    #         print ele.text;
    #         print ele.get_attribute("href")
            pass
        elif u"2017年11月杭州市小客车增量指标摇号结果公告" in ele.text:
            print ""
            urls = ele.get_attribute("href");
            driver = webdriver.Firefox(executable_path="/Users/yangjie/Downloads/chrome/geckodriver") 
            driver.get(urls); 
            ele = driver.find_element_by_xpath("//a[@attachid]")
            driver.get(ele.get_attribute("href"))
            running = False
            break

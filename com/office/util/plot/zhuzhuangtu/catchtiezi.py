#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
import sys
from com.office.util.excelUtil import writeExcel
reload(sys)
sys.setdefaultencoding('UTF-8')
import time

executable_path="/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver"
from selenium import webdriver
driver = webdriver.Chrome(executable_path)
time.sleep(0.1)
driver.get("http://www.19lou.com/forum-269-thread-6351469074427906-1-1.html")
time.sleep(0.1)

d = {}
while True:
    #找出当前页的所有名字
    nameEles = driver.find_elements_by_xpath("//*[@id='view-bd']/div/div[@class='side']/div/div/a/span");
    for nameEle in nameEles:
        name = nameEle.text.strip()
        if not d.has_key(name):
            d[name] = 0
        d[name] += 1
    #点击下一页
    try:
        driver.find_element_by_xpath('//*[@id="view-wrap"]/div/div/a[@class="page-next"]').click();
        print "next", len(d)
    except:
        break
        pass
        
resultDate = [[],[]]
for key in d:
    resultDate[0].append(key);
    resultDate[1].append(d[key]);
driver.quit()
writeExcel(resultDate, "resulttiezi2.xls");
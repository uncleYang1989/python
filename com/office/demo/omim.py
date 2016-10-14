#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年10月11日

@author: Administrator
'''
from com.office.util.codeUtil import forbidCodeErr
from com.office.util.pubUtil import retry
from com.office.util import fileUtil
forbidCodeErr()
from selenium import webdriver

def getPro(key):
    url="http://omim.org/entry/"+key
    print url
    driver.get(url)
    try:
        driver.find_element_by_id("donationClose").click()
    except Exception,e:
        pass;
    description = "";
    clinicalFeatures = "";
    try:
        retry(lambda:driver.find_element_by_xpath("//td[@id='floatingEntryContainer']/table/tbody/tr/td"))
        tdEles =driver.find_elements_by_xpath("//td[@id='floatingEntryContainer']/table/tbody/tr/td")
        for i in range(len(tdEles)):
            if tdEles[i].get_attribute("id") == "description":
                description = tdEles[i+1].text;
            elif tdEles[i].get_attribute("id") == "clinicalFeatures":
                clinicalFeatures = tdEles[i+1].text;
    except Exception, e:
        print e
    f2.write(key+"\t"+description+"\r" + clinicalFeatures+ "\n")   
f1=open("omim-id","r") .readlines()
f2=open("omim-description","a")      
driverPathname="/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver"
driver = webdriver.Chrome(driverPathname)
for omim in f1:
    key=omim.strip()
    print key
    getPro(key)
driver.quit()

  
    
            
            
    
     
        

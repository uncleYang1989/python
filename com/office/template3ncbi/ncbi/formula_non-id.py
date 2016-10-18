#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年10月16日

@author: Administrator
'''
from com.office.util.codeUtil import forbidCodeErr
from selenium import webdriver
from com.office.baike.FlowInfo import FlowInfo
from com.office.util.pubUtil import retry
from com.office.util.excelUtil import write

forbidCodeErr()
pubChem=FlowInfo("ncbi2.ini")
driver = pubChem.driver;
driver.get("https://www.ncbi.nlm.nih.gov/pccompound")
mylists=pubChem.keys
result=[]
def getchemID(key):
    while True:
        if driver.current_url=="https://www.ncbi.nlm.nih.gov/pccompound":
            chat=driver.find_element_by_id("term")
            chat.clear()
            chat.send_keys(key)
            driver.find_element_by_id("search").click()
            try:
                retry(lambda:driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"))
                ID1=driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
                result.append([key,ID1])
                driver.back()
                break
            except Exception,e:
                print e
            try:
                retry(lambda:driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a"))
                myTagas=driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a")
                key.upper()
                if len(myTagas)==0:                
                    result.append([key,"NA","NA"])
                    break;
                else:
                    for myTaga in myTagas:
                        if key.upper() in myTaga.text.upper():
                            href=myTaga.get_attribute("href")
                            drivercontent=webdriver.Chrome("/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver")
                            drivercontent.get(href)
                            retry(lambda:drivercontent.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"))
                            ID2=drivercontent.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
                            result.append([key,ID2])
                            drivercontent.quit()
                            return
                        else:
                            pass
            except Exception,e:
                result.append([key,"NA"])
                print e
                break;
        else:
            driver.get("http://www.ncbi.nlm.nih.gov/pccompound")
        
# for key in mylists:
#         try:
key = "C15H22O2"
print "处理",key
getchemID(key)
#             write(result, pubChem.resultPathname)
#             write(pubChem.recorddata,pubChem.recordPathname) 
#         except Exception,e:
#             print e
            
 

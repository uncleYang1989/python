#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年10月13日

@author: Administrator
'''
from com.office.util.codeUtil import forbidCodeErr
from com.office.util.pubUtil import retry
forbidCodeErr()
from selenium import webdriver

f1=open("lost_formula","r") .readlines()
f2=open("lost_formula_chikey","a")      
driverPathname="C:/Users/Administrator/Desktop/python/chromedriver_2.21/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(driverPathname)
driver.get("http://www.ebi.ac.uk/chebi/searchId.do;jsessionid=A37B456E96FF7E7E803B8DC1E1A17555?chebiId=CHEBI:66655")
def getPro(key,myid):   
    text="" 
    retry(lambda:driver.find_element_by_id("local-searchbox"))
    driver.find_element_by_id("local-searchbox").send_keys(key)
    retry(lambda:driver.find_element_by_class_name("submit"))
    driver.find_element_by_class_name("submit").click()
    try:
        chiTbls=driver.find_elements_by_xpath("//td[@class='gridLayoutCellTitle']/a")
        a_text=chiTbls[0].text
        print a_text
        if a_text.lower()==key.lower():
            Url=chiTbls[0].get_attribute("href")
            fi=driver.get("http://www.ebi.ac.uk/chebi/"+Url)
            chikey=driver.find_elements_by_class_name("chebiDataHeader")
            text=chikey[1].text
            print text
            fi.quit()
    except Exception, e:
        print e
        pass;
    f2.write(str(myid)+"\t"+str(key)+"\t"+text+"\n") 
for name in f1:
    name=name.split("\t")
    key=name[1]
    myid=name[0]
    getPro(key,id)
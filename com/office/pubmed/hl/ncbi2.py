#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月27日

@author: Administrator
'''
from com.office.util.codeUtil import forbidCodeErr
from selenium import webdriver
from com.office.util.pubUtil import retry
from com.office.util.excelUtil import write
from com.office.pubmed.hl.FlowInfo import FlowInfo

forbidCodeErr()
pubChem=FlowInfo("ncbi2.ini")
driverPathname=pubChem.driverPathname
driver = webdriver.Firefox()
driver.get("http://www.ncbi.nlm.nih.gov/pccompound")
mylists=pubChem.srcKeys
result=[]
def getchemID(key):
    while True:
        if driver.current_url.endswith("www.ncbi.nlm.nih.gov/pccompound"):
            chat=driver.find_element_by_id("term")
            chat.clear()
            chat.send_keys(key)
            driver.find_element_by_id("search").click()
            
            try:
                retry(lambda:driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"))
                ID1=driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
                trEles=driver.find_elements_by_xpath("//table[@class='top-summary-items']/tbody/tr")
                Molecular1 = ""
                if len(trEles) > 0:
                    for trEle in trEles:
                        thName = trEle.find_element_by_tag_name("th").text;
                        if "Molecular Formula" in thName:
                            Molecular1 = trEle.find_element_by_tag_name("td").text;
                            break
                print Molecular1
                result.append([key,ID1,Molecular1])
                pubChem.recorddata.append([key])
                driver.back()
                break
            except Exception,e:
                print "1", e
                import traceback
                print traceback.format_exc()
            try:
                retry(lambda:driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a"))
                myTagas=driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a")
                for myTaga in myTagas:
                    if key.upper() in myTaga.text.upper():
                        href=myTaga.get_attribute("href")
                        drivercontent=webdriver.Chrome(driverPathname)
                        drivercontent.get(href)
                        retry(lambda:drivercontent.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"))
                        ID2=drivercontent.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
                        Moleculars1=drivercontent.find_elements_by_xpath("//table[@class='top-summary-items']/tbody/tr/td/a")
                        Molecular2=Moleculars1[1].text
                        result.append([key,ID2,Molecular2])
                        pubChem.recorddata.append([key])
                        drivercontent.quit()
                        return
            except Exception,e:
                result.append([key,"NA","NA"])
                pubChem.recorddata.append([key])
                break
        else:
            driver.get("http://www.ncbi.nlm.nih.gov/pccompound")
mylists.reverse()
for key in mylists:
    if key in pubChem.recorddata:
        print "chuliguo"
        continue;
    else:
        try:
            key=key[0]
            print "处理",key
            getchemID(key)
            write(result, pubChem.resultPathname)
            write(pubChem.recorddata,pubChem.recordPathname) 
        except Exception,e:
            import traceback
            print traceback.format_exc()
            print "3", e
            
 

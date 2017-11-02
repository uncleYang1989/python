#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2017年5月10日

@author: Administrator
'''
from selenium import webdriver
from com.office.util.pubUtil import retry
driver = webdriver.Firefox()

f1=["ageratoside a 1", "ageratoside a 4", "agave cantala saponin 1"]
f2=open("result","a")
f3=open("fail","a")
def doSomething(keyword):
    key = keyword;
    
    driver.get("https://www.ncbi.nlm.nih.gov/pccompound/?term="+keyword);
    retry(lambda:driver.find_element_by_id("msgportlet"));
    try:
        msgEle = driver.find_element_by_id("msgportlet");
        if "No items found." in msgEle.text:
            f3.write(key)
            return
    except Exception,e:
        del e
        
    try:
        retry(lambda:driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"))
        resID=driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
        cs =""
        try:
            retry(lambda:driver.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div/div[@class="section-content-item"]'))
            cs=driver.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div/div[@class="section-content-item"]').text
            Names=driver.find_element_by_class_name("breakword").text
        except Exception,e:
            del e
            pass
        f3.write(key+"\t"+driver.current_url+"\t"+resID+"\t"+cs+"\t"+Names+"\n")
        return
    except Exception,e:
        del e
    retry(lambda:driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a"))
    myTagas=driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a")
    for myTaga in myTagas:
        if key.upper() in myTaga.text.upper():
            href=myTaga.get_attribute("href")
            from selenium import webdriver
            drivercontent=webdriver.Firefox()
            drivercontent.get(href)
            retry(lambda:drivercontent.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"))
            resID=drivercontent.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
            cs =""
            retry(lambda:drivercontent.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div/div[@class="section-content-item"]'))
            cs=drivercontent.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div/div[@class="section-content-item"]').text
            Names=driver.find_element_by_class_name("breakword").text
            f3.write(key+"\t"+href+"\t"+resID+"\t"+cs+"\t"+Names+"\n")
            drivercontent.quit();
            return
    f3.write(key)
for line in f1:
    key=line.strip()
    try:
        doSomething(key)
    except Exception,e:
        print e
        f3.write(key)
f2.close()
f3.close()   
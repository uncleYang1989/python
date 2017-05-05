#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2017年4月19日

@author: Administrator
'''
import requests 
from bs4 import BeautifulSoup
import csv

import sys

reload(sys)

sys.setdefaultencoding('utf-8')


f=open("fail-name","r")
f1=open("fail-result","wb")

for ts in f:
    ts=ts.strip().split("\t")
#     url="http://unpd.chem960.com/TcmList.aspx?key="+ts[1]
    url="http://unpd.chem960.com/TcmList.aspx?key="+"(1s,2s,4r,8s)-p-menthane-1,2,8,9-tetrol"
    re=requests.get(url, headers={'Connection':'close'})
    soup = BeautifulSoup(re.text,"html.parser")
    
    divs=soup.find_all("div", class_='cas_basea')
    #print(len(divs))
    processeds = []
    for div in divs:
        lis=div.find_all("li")
        a=div.find("a")
        link="http://unpd.chem960.com"+a['href']
        print link
        if link not in processeds:
            processeds.append(link)
            re2=requests.get(link, headers={'Connection':'close'})
            soup2 = BeautifulSoup(re2.text,"html.parser")
            divs=soup2.find_all("div", class_='basecont')
            if divs:
                result = str(divs[0]).split("InChI Key：")[1].split("<br>")[0]
    print ts[0]
    break
f1.close()
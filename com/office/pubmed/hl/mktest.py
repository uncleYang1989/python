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
f=open("fail-name","wb")
for i in range(100):
    f.write("%d\t%d\n"%(i,i))
f.close()
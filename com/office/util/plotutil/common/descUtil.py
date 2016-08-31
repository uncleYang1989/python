#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年7月17日

@author: yangjie
'''
from com.office.util.excelUtil import read
import matplotlib.pyplot as plt
def parseDesc(filename):
    descData = read(filename)
    descDict = {}
    for row in descData:
        try:
            descDict[row[0]] = row[1:]
        except Exception, e:
            print e
    
    #init xlabel
    if descDict.has_key("xlabel"):
        plt.xlabel(descDict["xlabel"][0])
    #init ylabel
    if descDict.has_key("ylabel"):
        plt.ylabel(descDict["ylabel"][0])
    #init title
    if descDict.has_key("title"):
        plt.title(descDict["title"][0], color='r', fontsize="xx-small",loc="right")
    return descDict;

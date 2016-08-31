#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
from com.office.util.excelUtil import read

tableData = read("/Users/yangjie/Desktop/juece2.xlsx")
print tableData

mainMap = {}
judgeRed = tableData[0][1]
judgeSize = tableData[0][2]
tableData = tableData[1:]
for rowData in tableData:
    name,hong, da, result = rowData
    print name,hong,da, result
    
    if not mainMap.has_key(judgeRed):
        mainMap[judgeRed] = {};
    tmpMap = mainMap[judgeRed]
    
    if not tmpMap.has_key(judgeSize):
        tmpMap[judgeSize] = {};
    tmpDaMap = tmpMap[judgeSize]
    tmpDaMap[da] = {"d":"d"}
    

from juece import createPlot
print mainMap
createPlot(mainMap)

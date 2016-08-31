#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
from com.office.util.excelUtil import read

tableData = read("/Users/yangjie/Desktop/juece.xlsx")
print tableData

mainMap = {}
judgeRed = tableData[0][1]
tableData = tableData[1:]
for rowData in tableData:
    name,hong,result = rowData
    print name,hong,result
    if not mainMap.has_key(judgeRed):
        mainMap[judgeRed] = {};
    tmpMap = mainMap[judgeRed]
    tmpMap[hong] = result

from juece import createPlot
print mainMap
createPlot(mainMap)

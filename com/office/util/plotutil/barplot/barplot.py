#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
import numpy
from com.office.util.excelUtil import read
from com.office.util.plotutil.common.colorUtil import getRandomColor
from com.office.util.plotutil.common.descUtil import parseDesc
fig, axes = plt.subplots()
all_data = read('barplot.xls');
for i in range(len(all_data)):
    for y in range(len(all_data[i])):
        if "" == all_data[i][y]:
            all_data[i] = all_data[i][:y];
            break

descDict = parseDesc('desc.xls')


if descDict.has_key("xaxisgrid"):
    axes.xaxis.grid(True)
if descDict.has_key("yaxisgrid"):
    axes.yaxis.grid(True)

if descDict.has_key("colors"):
    colors = descDict["colors"]
else:
    colors = getRandomColor(len(all_data))
barList = []
xticklist = all_data[0]
xVal=numpy.arange(len(xticklist))
barwidth=0.2
barSetp=0.2
curBarOffset = 0
plt.xticks(xVal+barwidth*2+barSetp,xticklist,rotation=79)
typeList = []

for vallist, color in zip(all_data[1:], colors):
    curBarOffset = curBarOffset + barSetp
    curXVal = xVal+barwidth+curBarOffset
    for x,y in zip(curXVal,vallist):
        plt.text(x, y, y, color=color)
    curType = plt.bar(curXVal,vallist,width=barwidth,color=color, edgecolor='#ffffff')
    typeList.append(curType)
if descDict.has_key("legend"):
    legend = descDict["legend"]
    plt.legend(typeList,legend, loc=0)
    
plt.show()

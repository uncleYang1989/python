#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
from com.office.util.excelUtil import read
from com.office.util.plotutil.common.colorUtil import getRandomColor
from com.office.util.plotutil.common.descUtil import parseDesc
fig, axes = plt.subplots()
all_data = read('scatterplot.xls');
descDict = parseDesc('desc.xls')

if descDict.has_key("xaxisgrid"):
    axes.xaxis.grid(True)
if descDict.has_key("yaxisgrid"):
    axes.yaxis.grid(True)
xlistList = []
ylistList = []
for i in range(len(all_data)/2):
    xlistList.append(all_data[i]);
    ylistList.append(all_data[i+1]);


if descDict.has_key("colors"):
    colors = descDict["colors"]
else:
    colors = getRandomColor(len(all_data))
barList = []
xticklist = all_data[0]
typeList = []

for xlist, ylist, color in zip(xlistList, ylistList, colors):
    curType = plt.scatter(xlist, ylist, s=20, c=color)#s (点的大小)
    typeList.append(curType)
    
if descDict.has_key("legend"):
    legend = descDict["legend"]
    plt.legend(typeList,legend, loc=0)
    
plt.show()

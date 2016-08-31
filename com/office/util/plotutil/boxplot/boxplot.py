#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
from com.office.util.excelUtil import read
from com.office.util.plotutil.common.colorUtil import getRandomColor
from com.office.util.plotutil.common.descUtil import parseDesc
fig, axes = plt.subplots()
all_data = read('boxplot.xls');
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
bplot = plt.boxplot(all_data,
            notch=False, # box instead of notch shape
            sym='rs', # red squares for outliers
            vert=True,
            patch_artist=True) # vertical box aligmnent

#init color
if descDict.has_key("colors"):
    colors = descDict["colors"]
else:
    colors = getRandomColor(len(all_data))
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

#init xticks
if descDict.has_key("xticks"):
    plt.xticks([y + 1 for y in range(len(all_data))], descDict["xticks"])

plt.show()

#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
from com.office.util.excelUtil import read
from matplotlib.colors import LogNorm
from pylab import hist2d, colorbar
from com.office.util.plotutil.common.descUtil import parseDesc
fig, axes = plt.subplots()
all_data = read('scatterplot.xls');
descDict = parseDesc('desc.xls')

if descDict.has_key("xaxisgrid"):
    axes.xaxis.grid(True)
if descDict.has_key("yaxisgrid"):
    axes.yaxis.grid(True)
xlistList = all_data[0]
ylistList = all_data[1]

hist2d(xlistList, ylistList, bins=80, norm=LogNorm())#bins 数值越大，点越小
colorbar()

plt.show()

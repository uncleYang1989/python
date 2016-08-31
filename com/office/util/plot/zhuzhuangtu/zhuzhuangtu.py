#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import numpy
import pylab
from com.office.util.excelUtil import read
from matplotlib import rcParams
pylab.figure(figsize=(9,6), dpi=80,edgecolor='y')
srcData = read("resulttiezi.xls");
keylist=srcData[0][:6]
vallist=srcData[1][:6]
barwidth=0.2
xVal=numpy.arange(len(keylist))/3.0
print xVal
print xVal+barwidth
pylab.xticks(xVal+barwidth+0.1,keylist,rotation=25)
pylab.bar(xVal+barwidth,vallist,width=barwidth,color='#FFFF00', edgecolor='#8B2252')
pylab.title(u'测试分析图',loc="right")
pylab.show()

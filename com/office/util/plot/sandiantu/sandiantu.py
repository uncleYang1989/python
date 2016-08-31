#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
from matplotlib.colors import LogNorm
from pylab import hist2d, colorbar
import matplotlib.pyplot as plt
from com.office.util.excelUtil import read
from com.office.util import fileUtil
import os
srcFiles =  fileUtil.getFiles("yaohao")
    
x = []
y = []
for srcFile in srcFiles[:5]:
    print "parse",srcFile
    srcData = read(os.path.join("yaohao", srcFile));
    src=[]
    d = {}
    for data in srcData[0]:
        datar = int(data)/100000000000
        if not d.has_key(datar):
            d[datar] = 0
        d[datar] += 1

    for key in d:
        y.append(d[key])
        x.append(key)
print x
print y
hist2d(x, y, bins=80, norm=LogNorm())
colorbar()
plt.show()
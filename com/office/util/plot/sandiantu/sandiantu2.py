#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
from com.office.util.excelUtil import read
from com.office.util import fileUtil
import os, random
srcFiles =  fileUtil.getFiles("yaohao")
    
plt.figure(figsize=(8, 5), dpi=150)
axes = plt.subplot(111)
typelist = []
descList= []
import numpy as np
from matplotlib.colors import colorConverter


def pastel(colour, weight=2.4):
    """ Convert colour into a nice pastel shade"""
    rgb = np.asarray(colorConverter.to_rgb(colour))
    # scale colour
    maxc = max(rgb)
    if maxc < 1.0 and maxc > 0:
        # scale colour
        scale = 1.0 / maxc
        rgb = rgb * scale
    # now decrease saturation
    total = rgb.sum()
    slack = 0
    for x in rgb:
        slack += 1.0 - x

    # want to increase weight from total to weight
    # pick x s.t.  slack * x == weight - total
    # x = (weight - total) / slack
    x = (weight - total) / slack

    rgb = [c + (x * (1.0 - c)) for c in rgb]
    return rgb
def get_colours(n):
    """ Return n pastel colours. """
    base = np.asarray([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    if n <= 3:
        return base[0:n]

    # how many new colours to we need to insert between
    # red and green and between green and blue?
    needed = (((n - 3) + 1) / 2, (n - 3) / 2)

    colours = []
    for start in (0, 1):
        for x in np.linspace(0, 1, needed[start] + 2):
            colours.append((base[start] * (1.0 - x)) +
                           (base[start + 1] * x))

    return [pastel(c) for c in colours[0:n]]
lens = 10;
srcFiles = srcFiles[:lens]
cs =  get_colours(lens-1)
print cs
for srcFile, c in zip(srcFiles, cs):
    x = []
    y = []
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
        
    print c
    print "x","y"
    print "x","y"
    typelist.append(plt.scatter(x, y, s=20, c=c))
    descList.append(srcFile);
    
plt.legend(typelist,descList)
plt.xlabel(u'中签号码的开头两位数')
plt.ylabel(u'中签个数')
plt.title(u"摇号散点图")
plt.show()




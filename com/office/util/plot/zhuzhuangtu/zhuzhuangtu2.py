#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import numpy
import pylab
from com.office.util.excelUtil import read
import os
from com.office.util import fileUtil
srcFiles =  fileUtil.getFiles("../sandiantu/yaohao")
d = {}
for srcFile in srcFiles[:5]:
    srcData = read(os.path.join("../sandiantu/yaohao", srcFile));
    src=[]
    print len(srcData[0])
    for data in srcData[0]:
        datar = int(data)/100000000000
        if not d.has_key(datar):
            d[datar] = 0
        d[datar] += 1

keylist = []
vallist = []
vallist2 = []
vallist3 = []
count = 10
fig, axes = pylab.subplots(nrows=1,ncols=2, figsize=(12,5))

for key in d:
    if count <0:
        break
    else:
        count-=1
    vallist.append(d[key])
    vallist2.append(d[key])
    vallist3.append(d[key])
    if key < 10:
        key = "0%d"%key
    else:
        key = str(key) 
    keylist.append(key)
    
vallist2 = numpy.array(vallist2)*2.9
vallist3 = numpy.array(vallist3)*1.7
barwidth=0.2
xVal=numpy.arange(len(keylist))
pylab.xticks(xVal+barwidth,keylist,rotation=79)
axes[0].yaxis.grid(True)
type1 = pylab.bar(xVal+barwidth,vallist,width=barwidth,color='y', edgecolor='#ffffff')
type2 = pylab.bar(xVal+barwidth+0.1,vallist2,width=barwidth,color='b', edgecolor='#ffffff')
type3 = pylab.bar(xVal+barwidth+0.2,vallist3,width=barwidth,color='r', edgecolor='#ffffff')

print xVal
print vallist

# for i in range(len(xVal)):
#     x = xVal[i]
#     y = vallist[i]
        
for x,y in zip(xVal,vallist):
    pylab.text(x+0.2, y+10, y, color="#abcdef")
for x,y in zip(xVal,vallist2):
    pylab.text(x-0.2, y+20, "hong:"+str(y), color="#abcdef",  fontsize='xx-large')

pylab.text(3, 180, u"啊哈哈哈哈", color="#abcdef")
pylab.legend((type1,type2,type3),("hehe","heihei","haha"), loc=0, fontsize='xx-small', title='iTitle')
pylab.title(u'摇号分布')
pylab.xlabel(u'中签号码的开头两位数')
pylab.ylabel(u'中签个数')
pylab.show()

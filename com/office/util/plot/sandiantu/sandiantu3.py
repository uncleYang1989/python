#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
import numpy as np
from com.office.util.excelUtil import write
plt.figure(figsize=(9,6), dpi=100)
n=100
#rand 均匀分布和 randn高斯分布
r = []
for i in range(6):
    x=np.random.randn(1,n)
    r.append(x[0])
write(r, "scatterplot.xls")

print x
y=np.random.randn(1,n)
print y
T=np.arctan2(x,y)
print T
plt.scatter(x,y,c=T,s=25,alpha=0.4,marker='o')
#T:散点的颜色
#s：散点的大小
#alpha:是透明程度
plt.show()



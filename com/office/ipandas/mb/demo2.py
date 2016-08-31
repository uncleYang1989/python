#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as col


'''
初始化行列的数据
'''
column_labels = list('AACD')
row_labels = list('WXYY')
data = np.random.rand(4,4)
print data
'''
设置渐变的颜色
1.设置两种颜色。比如说白色和红色，白色为开始色，数值由大到小就是由红变白
2.设置三种颜色，比如白色绿色红色，设置白色为中间色，绿色为开始色，
则数据由小到大会先绿色变白色再变红色
'''
startcolor = '#ffffff'  # a dark green 
# midcolor = '#ffffff'    # a bright white
endcolor = '#191970'    # a dark red
Mycmap = col.LinearSegmentedColormap.from_list('MyColorbar',[startcolor,endcolor])#use the "fromList() method

fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=Mycmap)
# heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(row_labels, minor=True)
ax.set_yticklabels(column_labels, minor=False)

plt.show()
# plt.savefig("/Users/yangjie/Documents/tmp/demo3.png")
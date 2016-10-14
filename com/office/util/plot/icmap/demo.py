#!/usr/bin/env python
# 
# from matplotlib.widgets import Cursor
# import numpy as np
# import matplotlib.pyplot as plt
# 
# 
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, axisbg='#FFFFCC')
# 
# x, y = 4*(np.random.rand(2, 100) - .5)
# ax.plot(x, y, 'o')
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2, 2)
# 
# # set useblit = True on gtkagg for enhanced performance
# cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
# 
# plt.show()
s = 163.68
a = 54200
d = 0
for i in range(30):
    d += (a) * 0.0003
print d
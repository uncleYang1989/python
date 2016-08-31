#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import matplotlib.pyplot as plt
import numpy as np

all_data = [np.random.normal(0, std, 10) for std in range(1, 4)]

print all_data
all_data = [[ 2.01942427,  0.28940582, -0.26911015, -0.40534984, -0.76939296,
       -0.37672719, -0.11786661,  0.17915547,  0.43019828,  0.7103858 ], 
            ]
fig = plt.figure(figsize=(8, 6))

bplot = plt.boxplot(all_data,
            notch=False, # box instead of notch shape
            sym='rs', # red squares for outliers
            vert=True,
            patch_artist=True) # vertical box aligmnent
colors = ['pink', 'lightblue', '#abcdef']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
print [y + 1 for y in range(len(all_data))]
plt.xticks([y + 1 for y in range(len(all_data))], ['x1', 'x2', 'x3'])
plt.xlabel('measurement x')
t = plt.title('Box plot')
plt.show()

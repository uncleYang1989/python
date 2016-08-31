#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
'''
【程序21】 
题目：求1+2!+3!+...+20!的和 
1.程序分析：此程序只是把累加变成了累乘。 
'''

count = 10;
r = 0;
z = 1;
for i in range(1, count+1):
    z = z * i
    r += z
print r

'''
1
2
6
24
120
720
5040
40320
362880
3628800
4037913
'''
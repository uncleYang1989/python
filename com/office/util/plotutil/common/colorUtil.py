#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年7月17日

@author: yangjie
'''
import random

def getRandomColor(num):
    resultColors = []
    while len(resultColors) < num:
        c = "#%x%x%x"%(random.randint(16, 255), random.randint(16, 255), random.randint(16, 255))
        resultColors.append(c);
        resultColors = list(set(resultColors))
    return resultColors;


if __name__ == "__main__":
    print getRandomColor(5)
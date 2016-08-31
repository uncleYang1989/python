#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年5月25日

@author: yangjie
'''

def forbidCodeErr():
    import sys
    reload(sys)
    sys.setdefaultencoding('UTF-8')
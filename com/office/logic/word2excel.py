#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
from com.office.util.excelUtil import write
from com.office.util.wordUtil import readDocx

content = readDocx("/Users/yangjie/Downloads/qq/(最完整版)胡希恕讲伤寒论.docx")
lines = content.split(u"。")
resultData = []
for line in lines:
    resultData.append([line])
write(resultData, "/Users/yangjie/Downloads/qq/(最完整版)胡希恕讲伤寒论.xls")

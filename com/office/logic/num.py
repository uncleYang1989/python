#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
from com.office.util.excelUtil import write
resultDate = []
for i in range(3):
    resultDate.append(range(3))
    
print resultDate

write(resultDate, "num.xls")
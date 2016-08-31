#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
from com.office.util.excelUtil import read, write
srcDate = read("六神曲.xlsx")
srcDate = srcDate[1:]
cache = []
lastSrc = ""
for rowDate in srcDate:
    if rowDate[2] != "":
        cacheline = []
        cacheline.append(rowDate[2])
        if rowDate[3] != "":
            lastSrc = rowDate[3]
        cacheline.append(lastSrc)
        cache.append(cacheline)

resultDate = []
for rowDate in srcDate:
    newLine = []
    newLine.append(rowDate[0])
    if rowDate[1] != "":
        newLine.append(rowDate[1])
        newLine.append("TCMID")
    else:
        if len(cache) != 0:
            takeCache = cache[0]
            cache.remove(takeCache)
            newLine.extend(takeCache)
    resultDate.append(newLine)

for cacheData in cache:
    newLine = []
    newLine.append("")
    newLine.extend(cacheData)
    resultDate.append(newLine)

print resultDate
write(resultDate, "六神曲_res.xls")
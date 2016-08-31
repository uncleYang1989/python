#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
# from com.office.util.excelUtil import read
# 
# srcData = read("/Users/yangjie/mywork/workspace/mypython/com/office/logic/zhuzhuangtu.xlsx")
# d = {}
# names = srcData[0]
# values  = srcData[1]
# for i in range(len(names)):
#     d[names[i]] = values[i]
#  
# a = [1,2,3] 
# b = [2,2,2]
# for i in range(len(a)):
#     a[i] = a[i] + b[i]
# print "a", a
ad = {"a":2,"b":2,"c":3}
bd = {"a":2,"b":2,"c":3}
for key in ad:
    print "key", key, "value", ad[key]
    ad[key] = ad[key] + bd[key]
print ad
# 
# for key in d:
#     print key,"欠我", d[key],"元"

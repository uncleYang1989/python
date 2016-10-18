#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
from os.path import join
import commands
def writeFile(pathname, value, mode = 'wb'):
    f = open(pathname, mode)
    f.write(value)
    f.close()
def readFile(pathname, mode = 'rb'):
    f = open(pathname, mode)
    res = f.read()
    f.close()
    return res
def appendFile(pathname, value, mode = 'a'):
    f = open(pathname, mode)
    f.write(value)
    f.close()

def batchExtRename(dirName, oldExt, newExt):
    import os
    for f in os.listdir(dirName):
        if f.endswith(oldExt):
            old = os.path.join(dirName, f)
            new = os.path.join(dirName, f.replace(oldExt, newExt))
            os.rename(old, new)
def getKeyList(excelPathname, isAll = False, sheetName="Sheet1"):
    print "从［%s］中读取关键字.."%excelPathname
    import xlrd
    data = xlrd.open_workbook(excelPathname);
    table = data.sheet_by_name(sheetName)#通过名称获取
    nrows = table.nrows
    returnList = [];
    for i in range(nrows ):
        if isAll:
            returnList.append(table.row_values(i))
        else:
            returnList.append(table.row_values(i)[0])
    print "获得到%d个关键字"%len(returnList)
    return returnList;

def isFileAdd(targetDir, lastFileNames, fileTypeFitters = None):
    import os
    newFiles = []
    curFileNames = []
    isAdd = False
    
    for f in os.listdir(targetDir):
        curFileNames.append(f);
        if None != fileTypeFitters:
            isMatch = False
            for fileTypeFitter in fileTypeFitters:
                if  f.endswith(fileTypeFitter):
                    isMatch = True;
                    break
            if not isMatch:
                continue
        fileIndex = lastFileNames.find(f);
        if fileIndex == -1:
            newFiles.append(f);
    if len(newFiles) != 0:
        isAdd = True
    return isAdd, curFileNames, newFiles

def getFiles(targetDir, joinDir=False):
    import os
    curFileNames = []
    for f in os.listdir(targetDir):
        if joinDir:
            curFileNames.append(os.path.join(targetDir, f));
        else:
            curFileNames.append(f);
    return curFileNames
def cleardir(pathname, dirname = ""):
    if dirname:
        pathname = join(pathname, dirname)
    cmd = "rm -rf %s/* "%pathname
    output = commands.getoutput(cmd)
        
def mkdir(dirname):
    cmd = "mkdir -p %s "%dirname
    output = commands.getoutput(cmd)
if __name__ == "__main__":
    dirName = "/Users/yangjie/Documents/tmp/"
    import time
    while True:
        batchExtRename(dirName, ".csv", ".ttttt")
        time.sleep(2)
        batchExtRename(dirName, ".ttttt", ".csv")
        time.sleep(2)
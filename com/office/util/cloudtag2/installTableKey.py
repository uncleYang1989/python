#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
from com.office.util.excelUtil import read
from com.office.util.sqlUtil import save
from com.office.util import fileUtil
from com.office.util.fileUtil import readFile
import os
if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect("ios.db")
    targetDir = "/Users/yangjie/Library/Application Support/MobileSync/Backup/51b76fcdb07aca7b565b567a49c2f3bfdeaee000"
    filenames = fileUtil.getFiles(targetDir, True)
    save_sql = """insert into "main"."result" ( "first", "second", "third") values ( ?, ?, ?);"""
    data = []
    count = 0;
    for filename in filenames:
        content = readFile(os.path.join(targetDir, filename))
        data.append((filename,content,""))
        count += 1
        print count
        try:
            save(conn, save_sql, data)
        except:
            pass
        data=[]
    save(conn, save_sql, data)
    
    

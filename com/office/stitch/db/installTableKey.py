#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
from com.office.stitch.db import DATABASE_PATHNAME
from com.office.util.excelUtil import read
from com.office.util.sqlUtil import save
from com.office.util import fileUtil

if __name__ == "__main__":
#     import sqlite3
#     conn = sqlite3.connect(DATABASE_PATHNAME)
#     tableData = read(r"/Users/yangjie/Downloads/qq/ingredients_only.xls", "Sheet1");
#     save_sql = """insert into "main"."keys" ( "status", "keyword") values ( ?, ?);"""
#     data = []
#     for row in tableData:
#         keyword = row[0]
#         data.append((0,keyword))
#         if len(data) >=100:
#             save(conn, save_sql, data)
#             data=[]
#     save(conn, save_sql, data)
    import sqlite3
    conn = sqlite3.connect(DATABASE_PATHNAME)
    f1 = fileUtil.readFile("omim-id");
    save_sql = """insert into "main"."keys" ( "status", "keyword") values ( ?, ?);"""
    data = []
    for row in f1.split("\r"):
        keyword = row
        data.append((0,keyword))
        if len(data) >=100:
            save(conn, save_sql, data)
            data=[]
    save(conn, save_sql, data)
    
    

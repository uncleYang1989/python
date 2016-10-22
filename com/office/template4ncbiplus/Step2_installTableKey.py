#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
forbidCodeErr()
from com.office.util.sqlUtil import save
from com.office.util import fileUtil
from com.office.template2 import DBNAME
from com.office.util.excelUtil import read

if __name__ == "__main__":
    keywords = []
    srcpathname = r"/Users/yangjie/mywork/workspace/mypython/com/office/template4ncbiplus/db/update_pubid.xlsx"
    if srcpathname.endswith("xls") or srcpathname.endswith("xlsx"):
        tableData = read(srcpathname, "Sheet2");
        for row in tableData:
            if row[3] == u'Not Available':
                try:
                    keywords.append(row[4] +u"SPLITMARK"+row[6]);
                except Exception,e:
                    del e
    else:
        f1 = fileUtil.readFile(srcpathname);
        keywords = f1.split("\r\n");
        if len(keywords) < 2:
            keywords = f1.split("\r");
        if len(keywords) < 2:
            keywords = f1.split("\n");
    
    #上面的代码就是将原始数据转换城一个列表    
    
    data = []
    save_sql = """insert into "main"."keys" ( "status", "keyword") values ( ?, ?);"""
    import sqlite3
    conn = sqlite3.connect(DBNAME)
    conn.text_factory = str
    count = 0;
    for keyword in keywords:
        data.append((0,keyword))
        if len(data) >=1000:
            save(conn, save_sql, data)
            data=[]
            count += 1000
            print count,r"/",len(keywords);
    save(conn, save_sql, data)
    
    

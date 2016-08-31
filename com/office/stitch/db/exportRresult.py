#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
from com.office.util.sqlUtil import get_conn, fetchall
from com.office.util.excelUtil import write

if __name__ == "__main__":
    fetchall_sql = '''SELECT * FROM result'''
    conn = get_conn("/Users/yangjie/mywork/workspace/mypython/com/office/stitch/db/normal.db")
    results = fetchall(conn, fetchall_sql)
    tableData = []
    FILENAME = "../result/result_%d.xls";
    fileCount = 0;
    for result in results:
        tableData.append([result[1], result[2], result[3]])
        if len(tableData) > 65534:
            write(tableData, FILENAME%fileCount)
            fileCount+=1
            tableData = [];
    write(tableData, FILENAME%fileCount)
    

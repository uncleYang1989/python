#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
forbidCodeErr()
from com.office.util.excelUtil import read, writeExcel
import sqlite3
def getFromDB(keyword):
    conn = None
    try:
        conn = sqlite3.connect("/Users/yangjie/mywork/workspace/mypython/com/office/template4ncbiplus/db/ncbi1023.db")
        cu = conn.cursor()  
        select_sql = "select * from result where url='"+keyword+"' order by id desc limit 1";
        cu.execute(select_sql)  
        result = cu.fetchall()
        return result
    except Exception,e:
        del e
    finally:
        if conn:
            conn.close();
            
if __name__ == "__main__":
    keywords = []
    srcpathname = r"/Users/yangjie/mywork/workspace/mypython/com/office/template4ncbiplus/db/update_pubid.xlsx"
    src2pathname = r"/Users/yangjie/mywork/workspace/mypython/com/office/template4ncbiplus/db/update_pubid2.xlsx"
    destPathname = r"/Users/yangjie/mywork/workspace/mypython/com/office/template4ncbiplus/db/result1023_plus.xlsx"
    tableData = read(srcpathname, "Sheet2");
    table2Data = read(src2pathname, "Sheet2");
    resultTable = [];
    updateCount = 0;
    for row in tableData:
        for row2 in table2Data:
            if row[4] == row2[4]:
                row = row2;
                break;
        if row[3] == u'Not Available':
            result = getFromDB(row[4])
            if result:
                info = result[0][1:]
                row[3] = info[3]
                row[6] = info[2]
                row[7] = info[4]
                updateCount+=1;
        resultTable.append(row);
        if len(resultTable)%1000==0:
            print len(resultTable),r"/",len(tableData), r"-",updateCount
    print updateCount, r"/",len (tableData)
    writeExcel(resultTable, destPathname);

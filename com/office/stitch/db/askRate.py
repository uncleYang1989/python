#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
import sqlite3,time

if __name__ == "__main__":
    onBeginFinished=None;
    beginTime = int(time.time())
    while True:
        conn = None;
        try:
            conn = sqlite3.connect("normal.db")
            cu = conn.cursor()  
            select_sql = 'select count(0) from keys';
            cu.execute(select_sql)  
            result = cu.fetchall()
            total = result[0][0]
            select_sql = 'select count(0) from keys where status=2';
            cu.execute(select_sql)  
            result = cu.fetchall()
            finished = result[0][0]
            if onBeginFinished is None:
                onBeginFinished = finished
            select_sql = 'select count(0) from keys where status=1';
            cu.execute(select_sql)  
            result = cu.fetchall()
            inProcess = result[0][0]
            avg = ((finished-onBeginFinished)*3600)/(int(time.time())-beginTime)
            if avg:
                last = float(total - finished)/avg
            else:
                last = "unknown"
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),u"%d/%d(%f) 平均每小时处理[%s] 预计剩余[%s]小时完成 %d in Process"%(finished, total, float(finished)/total, avg, last, inProcess)
        finally:
            if conn:
                conn.close()
        time.sleep(5)
    
    

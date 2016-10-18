#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''
import copy, sys, os
def get_work_root():
    '''
    初始化工作目录
    '''
    sysPath = copy.copy(sys.path)
    for path in sysPath:
        workRoot = "";
        tmps = path.split(os.path.sep);
        if ("com" in tmps and "office" in tmps):
            for tmp in tmps[:tmps.index("com")]:
                workRoot += tmp;
                workRoot += os.path.sep;
            return workRoot
    return "";
sys.path.append(get_work_root())
import sqlite3,time
from com.office.template3ncbi import DBNAME

if __name__ == "__main__":
    onBeginFinished=None;
    beginTime = int(time.time())
    while True:
        conn = None;
        try:
            conn = sqlite3.connect(DBNAME)
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
            avg = None
            try:
                avg = ((finished-onBeginFinished)*3600)/(int(time.time())-beginTime)
            except Exception,e:
                pass
            if avg:
                last = float(total - finished)/avg
                last = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime( last*60*60+time.time()))
            else:
                last = "unknown"
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),u"%d/%d(%f) 平均每小时处理[%s] 预计完成时间[%s] %d in Process"%(finished, total, float(finished)/total, avg, last, inProcess)
        finally:
            if conn:
                conn.close()
        time.sleep(5)
    
    

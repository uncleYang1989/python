#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月1日

@author: Administrator
'''
import copy, sys, os, traceback
from urllib import quote
def get_work_root():
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

from com.office.util.codeUtil import forbidCodeErr
from com.office.util.sqlUtil import save
import sqlite3, time, threading
from com.office.util.pubUtil import doInThread, retry, doByTimeout


forbidCodeErr()
DATABASE_PATHNAME = "db/pub0707.db"
DIRVER_PATHNAME= "/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver"
URL=u"http://www.ncbi.nlm.nih.gov/pccompound/?term=%s"
processRange = [0, 19000]

STATUS_NON=0
STATUS_IN_PROCESS=1
STATUS_SUCCESS=2
STATUS_INIT_DRIVER=3

OVER_TIME_PROCESS=120
OVER_TIME_INIT_DRIVER=120

PROCESS_NUM=10


class PFlowInfo():
    def __init__(self, driver, needInitDriver, tableId, keyword):
        self.driver = driver
        self.needInitDriver = needInitDriver
        self.tableId = tableId
        self.keyword = keyword
        
def getOnWtitch(pfi):
    needInitDriver = pfi.needInitDriver;
    keyword = pfi.keyword;
    tableId = pfi.tableId;
    if needInitDriver:
        updateStatus(STATUS_INIT_DRIVER, tableId)
        try:
            if pfi.driver  is not None:
                pfi.driver .close()
        except Exception, e:
            pass
        try:
            if pfi.driver  is not None:
                pfi.driver .quit()
        except Exception, e:
            print 'quit error', e
        try:
            # #使用第三方库，模拟浏览器登录
            from selenium import webdriver
            pfi.driver = webdriver.Chrome(executable_path = DIRVER_PATHNAME)
        except Exception, e:
            print 'initDriver error', e
            updateStatus(STATUS_NON, tableId)
            return
        pfi.needInitDriver = False
        updateStatus(STATUS_IN_PROCESS, tableId)
    driver = pfi.driver 
    while True:
        try:
            raiseOnError = True;
            try:
                driver.get(URL%quote(keyword));
            except KeyError,ke:
                addResult([[keyword,"KEYERR","KEYERR"]])
                updateStatus(STATUS_SUCCESS, tableId)
                break
            time.sleep(0.1)
            isFind = True
            if driver.title.endswith("NCBI"):
                #result_count
                if retry(lambda:driver.find_element_by_id("result_sel"), times=10, allowError=True, raiseOnError=raiseOnError):
                    pass
                    #success
                else:
                    #error
                    updateStatus(STATUS_NON, tableId)
                    pfi.needInitDriver = True
                    break
            isFind = False
            retry(lambda:driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a"), times=10, allowError=True, raiseOnError=raiseOnError)
            myTagas=driver.find_elements_by_xpath("//div[@class='content']/div/div/div/div/p/a")
            for myTaga in myTagas:
                if keyword.upper() in myTaga.text.upper() or\
                    keyword.upper().replace(" ", "") in myTaga.text.upper().replace(" ", ""):
                    myTaga.click();
                    isFind = True
                    break;
            #TODO 是否需要翻页查询
            if not isFind:
                addResult([[keyword,"NA","NA"]])
                updateStatus(STATUS_SUCCESS, tableId)
                break
            retry(lambda:driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td"), times=1000, allowError=True, raiseOnError=raiseOnError)
            ID1=driver.find_element_by_xpath("//table[@class='top-summary-items']/tbody/tr/td").text
            Moleculars=driver.find_elements_by_xpath("//table[@class='top-summary-items']/tbody/tr/td/a")
            if len(Moleculars) > 1:
                Molecular1=Moleculars[1].text
            elif len(Moleculars) == 1:
                Molecular1=Moleculars[0].text
            else:
                Molecular1="NA"
            addResult([[keyword,ID1,Molecular1]])
            updateStatus(STATUS_SUCCESS, tableId)
            break
        except Exception, e:
            print "keyword:",keyword,traceback.format_exc()
            updateStatus(STATUS_NON, tableId)
            pfi.needInitDriver = True
            break
# query values from table  
def getAndUpdateNextKey():
    '''获取下一条Key'''
    conn = None;
    try:
        fetchone_sql = 'SELECT id, keyword FROM keys WHERE status=0 and id >= %d and id <= %d limit 1'%(processRange[0], processRange[1])
        conn = sqlite3.connect(DATABASE_PATHNAME)
        cu = conn.cursor()  
        cu.execute(fetchone_sql)  
        result = cu.fetchall()
        if result:
            tableId = result[0][0]
            update_sql = 'UPDATE keys set status=1 where id=%d' % tableId
            cu.execute(update_sql)
            conn.commit()
            return True, result[0];
        else:
            return False, None
    except Exception, e:
        print 'error', e  
        return False, None
    finally:
        if conn:
            conn.close()
            
def updateStatus(status, tableId=None):
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_PATHNAME)
        cu = conn.cursor()
        if tableId:
            update_sql = 'UPDATE keys set status=%d where id=%d;' % (status, tableId)
        else:
            update_sql = 'UPDATE keys set status=0 where status != %d;' % status
        cu.execute(update_sql)
        conn.commit()
        return True;
    except Exception, e:
        print 'update status error', e
        return False;
    finally:
        if conn:
            conn.close()
            
def addResult(data):
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_PATHNAME)
        save_sql = """insert into "result" ( "first", "second", "third") values ( ?, ?, ?);"""
        save(conn, save_sql, data)
        conn.commit()
        return True;
    except Exception, e:
        print 'add result  error', e
        return False;
    finally:
        if conn:
            conn.close()
            

def process(req):
    __lock, pid = req["lock"], req["pid"]
    time.sleep(pid)
    print u"worker[%d]开始工作" % pid
    pfi = PFlowInfo(None, True, None, None)
    while True:
        try:
            __lock.acquire()
            exist, reuslt = getAndUpdateNextKey();
            __lock.release()
            if not exist:
                print u"worker[%d]结束" % pid
                break
            tableId, keyword = reuslt
            
            pfi.keyword = keyword
            pfi.tableId  = tableId
            timeoutNum = OVER_TIME_PROCESS;
            if pfi.needInitDriver:
                timeoutNum += OVER_TIME_INIT_DRIVER;
            if not doByTimeout(getOnWtitch, pfi, timeoutNum):
                (STATUS_NON, tableId)
                print u"worker[%d]超时，进行重启" % pid
                pfi.needInitDriver = True
        except Exception,e:
            pfi.needInitDriver = True
            print 'process error', e, traceback.format_exc()
            
        
        
if __name__ == "__main__":
    __lock = threading.Lock()
    updateStatus(STATUS_SUCCESS, None)
    poolNum = PROCESS_NUM;
    arg_list = []
    for i in range(poolNum):
        req = {}
        req["lock"] = __lock;
        req["pid"] = i;
        arg_list.append(req)
    doInThread(process, arg_list, poolNum=poolNum)

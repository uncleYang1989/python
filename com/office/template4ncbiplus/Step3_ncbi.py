#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
'''#数据库的路径'''
from com.office.template4ncbiplus import DBNAME as DATABASE_PATHNAME
'''启动的进程数'''
PROCESS_NUM=1
'''#谷歌浏览器驱动的路径'''
DIRVER_PATHNAME= "/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver"
'''#要抓取的网站的URL'''
URL=""
'''#单个任务超时时间'''
OVER_TIME_PROCESS=120
'''启动浏览器的超时时间'''
OVER_TIME_INIT_DRIVER=120
'''#是否打印任务进度'''
IS_NEED_PRINT_RATE=False
'''#是否需要启动浏览器'''
IS_NEED_DRIVER=True
'''
增加结果信息到数据库调用方法 addResult
传入的对象必须是一个二维数组
例:
    addResult([['1','2','3']])

#更新任务状态调用方法 updateStatus
例:
    updateStatus(STATUS_SUCCESS, tableId)
'''
def doSomething(driver, keyword, tableId, pfi):
    name = keyword.split(u"SPLITMARK")[0];
    if len(keyword.split(u"SPLITMARK")) > 1:
        mf = keyword.split(u"SPLITMARK")[1];
    else:
        mf = ""
    try:
        driver.get("https://www.ncbi.nlm.nih.gov/pccompound/?term="+name);
    except Exception,e:
#         addResult([[keyword, name,mf,"None","None"]])
        updateStatus(STATUS_SUCCESS, tableId)
        return
    retry(lambda:driver.find_element_by_id("msgportlet"));
    try:
        msgEle = driver.find_element_by_id("msgportlet");
        if "No items found." in msgEle.text:
#             addResult([[keyword, name,mf,"None","None"]])
            updateStatus(STATUS_SUCCESS, tableId)
            return
    except Exception,e:
        del e
    
    
    resultEle = None
    try:
        resultEle = driver.find_element_by_class_name("title_and_pager");
    except Exception, e:
        del e
    if resultEle is None:
        retry(lambda:driver.find_element_by_id("msgportlet"));
        parseDetail(driver, mf, name, tableId,keyword);
        return
    else:
        retry(lambda:driver.find_elements_by_class_name("rsltcont"));
        rsltcontEles =driver.find_elements_by_class_name("rsltcont")
        if mf.strip() == u'Not Available' and len(rsltcontEles) != 1:
#             addResult([[keyword, name,mf,"None","None"]])
            updateStatus(STATUS_SUCCESS, tableId)
            return
        for rsltcontEle in rsltcontEles:
            if mf.upper() in rsltcontEle.text.upper() and name.upper() in rsltcontEle.text.upper():
                href=rsltcontEle.find_element_by_xpath("//p[@class='title']/a").get_attribute("href");
                driver.get(href);
                parseDetail(driver, mf, name, tableId,keyword);
                return
#     addResult([[keyword, name,mf,"None","None"]])
    updateStatus(STATUS_SUCCESS, tableId)


def parseDetail(drivercontent, mf, name, tableId,keyword):
    retry(lambda:drivercontent.find_elements_by_xpath("//table[@class='top-summary-items']/tbody/tr"))
    trEles=drivercontent.find_elements_by_xpath("//table[@class='top-summary-items']/tbody/tr")
    resID = ""
    onlineMF=""
    for trEle in trEles:
        tmp = trEle.text.split(":")
        if tmp[0] == u"PubChem CID":
            resID = tmp[1]
        elif tmp[0] == u"Molecular Formula":
            onlineMF = tmp[1]
            if mf.strip() and mf.strip() != u'Not Available' and onlineMF.strip().upper() != mf.strip().upper():
#                 addResult([[keyword, name,mf,"None","None"]])
                updateStatus(STATUS_SUCCESS, tableId)
                return
            if mf.strip() == u'Not Available':
                mf=onlineMF.strip().upper();
    if not resID:
        resID = drivercontent.current_url.split(r"#")[0].split(r"?")[0].split(r'/')[-1];
    retry(lambda:drivercontent.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div/div[@class="section-content-item"]'), times=100)
    cs=drivercontent.find_element_by_xpath('//*[@id="Canonical-SMILES"]/div/div[@class="section-content-item"]').text
    addResult([[keyword, name,mf,resID,cs]])
    updateStatus(STATUS_SUCCESS, tableId)
'''
以下为框架代码，不需要修改
'''

STATUS_NON=0
STATUS_IN_PROCESS=1
STATUS_SUCCESS=2
STATUS_INIT_DRIVER=3
import copy, sys, os, traceback
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
from com.office.util.codeUtil import forbidCodeErr
forbidCodeErr()
from com.office.util.sqlUtil import save
import sqlite3, time, threading
from com.office.util.pubUtil import doInThread, retry
class PFlowInfo():
    '''
    线程处理的消息共享对象
    '''
    def __init__(self, driver, needInitDriver, tableId, keyword):
        self.driver = driver
        self.needInitDriver = needInitDriver
        self.tableId = tableId
        self.keyword = keyword
        
def processInWorker(pfi):
    '''
    线程处理方法
    '''
    needInitDriver = pfi.needInitDriver;
    keyword = pfi.keyword;
    tableId = pfi.tableId;
    if needInitDriver and IS_NEED_DRIVER:
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
            print traceback.format_exc();
            print 'quit error', e
        try:
            # #使用第三方库，模拟浏览器登录
            from selenium import webdriver
            pfi.driver = webdriver.Chrome(executable_path = DIRVER_PATHNAME)
            if URL:
                pfi.driver.get(URL)
            
        except Exception, e:
            print traceback.format_exc();
            print 'initDriver error', e
            updateStatus(STATUS_NON, tableId)
            return
        pfi.needInitDriver = False
        updateStatus(STATUS_IN_PROCESS, tableId)
    driver = pfi.driver 
    try:
        doSomething(driver, keyword, tableId, pfi);
    except Exception,e:
        print 'error', e  
        print traceback.format_exc()
        updateStatus(STATUS_NON, tableId)
        pfi.needInitDriver = True
# query values from table  
def getAndUpdateNextKey():
    '''获取下一条Key'''
    conn = None;
    try:
        fetchone_sql = 'SELECT id, keyword FROM keys WHERE status=0 limit 1'
        conn = sqlite3.connect(DATABASE_PATHNAME)
        cu = conn.cursor()  
        cu.execute(fetchone_sql)  
        result = cu.fetchall()
        if result:
            tableId = result[0][0]
            update_sql = 'UPDATE keys set status=1 where id=%d;' % tableId
            cu.execute(update_sql)
            conn.commit()
            return True, result[0];
        else:
            return False, None
    except Exception, e:
        print 'error', e  
        print traceback.format_exc();
        return False, None
    finally:
        if conn:
            conn.close()
            
def updateStatus(status, tableId=None):
    '''
    更新数据库中关键字的状态，如未开始、已完成、进行中
    '''
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_PATHNAME)
        cu = conn.cursor()
        if tableId:
            update_sql = 'UPDATE keys set status=%d where id=%d ;' % (status, tableId)
        else:
            update_sql = 'UPDATE keys set status=0 where status != %d;' % status
        cu.execute(update_sql)
        conn.commit()
        return True;
    except Exception, e:
        print 'update status error', e
        print traceback.format_exc();
        return False;
    finally:
        if conn:
            conn.close()
            
def addResult(data):
    print data
    '''
    在result表中添加数据
    '''
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_PATHNAME)
        save_sql = """insert into "result" ( "keyword", "url", "result1", "result2", "result3") values ( ?, ?, ?, ?, ?);"""
        save(conn, save_sql, data)
        conn.commit()
        return True;
    except Exception, e:
        print 'add result  error', e
        print traceback.format_exc();
        return False;
    finally:
        if conn:
            conn.close()
            

def process(req):
    '''
    线程处理主函数
    '''
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
                print u"没有关键字需要处理,worker[%d]工作结束" % pid
                break
            tableId, keyword = reuslt
            pfi.keyword = keyword
            pfi.tableId  = tableId
            timeoutNum = OVER_TIME_PROCESS;
            if pfi.needInitDriver:
                timeoutNum += OVER_TIME_INIT_DRIVER;
            if doByTimeout(processInWorker, pfi, timeoutNum):
                if IS_NEED_PRINT_RATE:
                    print u"worker[%d]处理[%s]结束"%(pid, keyword)
            else:
                updateStatus(STATUS_NON, tableId)
                print u"worker[%d]超时，进行重启" % pid
                pfi.needInitDriver = True
                if IS_NEED_PRINT_RATE:
                    print u"worker[%d]处理关键字[%s]超时"%(pid, keyword)
        except Exception,e:
            print traceback.format_exc();
            pfi.needInitDriver = True
            print 'process error', e
            
def doByTimeout(callable__, arg, timeoutNum=60):
    '''
    允许设置超时时间的处理函数
    '''
    t = threading.Thread(target=callable__, args=(arg,))
    t.start()
    success = False
    timeoutNum = timeoutNum * 100;
    while timeoutNum > 0:
        if t.isAlive():
            timeoutNum -= 1;
            time.sleep(0.01);
        else:
            success = True
            break;
    return success; 
        
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

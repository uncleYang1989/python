#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8

    
def doInThread(callable_, argsList, poolNum=5):
    import threadpool
    pool = threadpool.ThreadPool(poolNum)
    requests = threadpool.makeRequests(callable_, argsList)
    for req in requests:
        pool.putRequest(req)
    pool.wait()

def retry(func, times=100, sleepSeconds=0.1, allowError=False, raiseOnError=False):
    import time
    lastE = None
    while times > 0:
        try:
            func();
        except Exception, e:
            lastE = e;
            times-=1;
            time.sleep(sleepSeconds)
        else:
            return True;
    if not allowError:
        print lastE
    if raiseOnError:
        raise Exception, "onerror"
    return False;

def doByTimeout(callable__, arg, timeoutNum=60):
    import threading, time
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
        

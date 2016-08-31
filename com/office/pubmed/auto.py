#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
from selenium import webdriver
from com.office.util.codeUtil import forbidCodeErr
from com.office.util.excelUtil import write, read
from selenium.webdriver.common.keys import Keys
from com.office.util.pubUtil import doInThread, retry
forbidCodeErr()

FILENAME_RECORD = "record.xls"
FILENAME_RESULT = "result.xls"
executable_path="/Users/yangjie/Documents/env/jyang-site-packages/chromedriver_2.21/chromedriver_mac32/chromedriver"
reusltData = []
try:
    reusltData = read(FILENAME_RESULT)
except Exception,e:
    print e

recoreDate=[]
matchRecordData=[]
try:
    recoreDate = read(FILENAME_RECORD)
    for row in recoreDate:
        matchRecordData.append(row[0])
except Exception,e:
    print e

'''
retry方法作用是对可能出错的代码进行最多100次的重试
'''
#初始化谷歌浏览器
def initDriver():
    driver = webdriver.Chrome(executable_path=executable_path)
    #跳到网址
    retry(lambda:driver.get("http://www.ncbi.nlm.nih.gov/pubmed/"))
    
    #填入查询字段
    keyword = "Worldviews On Evidence-Based Nursing"
    retry(lambda:driver.find_element_by_id("term").clear());
    retry(lambda:driver.find_element_by_id("term").send_keys(keyword))
    
    #点击查询按钮
    retry(lambda:driver.find_element_by_id("search").click());
    return driver;

driver = initDriver();


#定义查询语句
keys = ["aa", "rheumatic disease", "immune disease", "arthritis", "chinese medicine", "ankylosing spondylitis", "leukemia"]
def processInNewDriver(href):
    '''
    处理文章链接
    '''
    print "处理链接", href
    driverContent = webdriver.Chrome(executable_path=executable_path)
    driverContent.get(href)
      
    retry(lambda:driver.find_element_by_class_name("rprt_all"));
    contentEle = driverContent.find_element_by_class_name("rprt_all")
    content = contentEle.text
    for key in keys:
        if content.find(key) != -1:
            print "find"
            reusltData.append([href, key])
            write(reusltData, FILENAME_RESULT)
            break
    recoreDate.append([href])
    driverContent.quit()

while True:
    retry(lambda:driver.find_elements_by_xpath("//p[@class='title']/a"));
    aEles = driver.find_elements_by_xpath("//p[@class='title']/a")
    hrefs = []
    for aEle in aEles:
        href = aEle.get_attribute("href")
        if href in matchRecordData:
            print "processd ", href
        else:
            hrefs.append(href)
    if 0 == len(hrefs):
        print "no new href"
    else:
        doInThread(processInNewDriver, hrefs, poolNum=4)
        write(recoreDate, FILENAME_RECORD);
        
    try:
        driver.find_element_by_xpath("//a[@id='EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Entrez_Pager.Page' and @sid='3']").send_keys(Keys.ENTER);
        print "下一页"
        import time
        time.sleep(1)
    except Exception,e:
        print "已到尾页"
        break;



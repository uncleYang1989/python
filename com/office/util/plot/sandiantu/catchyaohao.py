#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
import copy, sys, os
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
from com.office.util.excelUtil import  writeExcel
from selenium.webdriver.support.select import Select
from com.office.util.pubUtil import retry
reload(sys)
sys.setdefaultencoding('UTF-8')
import time

from selenium import webdriver  
profile = webdriver.FirefoxProfile()  
profile.set_preference("browser.startup.homepage", "about:blank")  
profile.set_preference("startup.homepage_welcome_url", "about:blank")  
profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")  
profile.update_preferences()  
driver = webdriver.Chrome(executable_path="/Users/yangjie/mywork/icode/cloudnms/sky-auto/autouitest/driver/chrome/chromedriver_mac32/chromedriver")  
time.sleep(0.1)
driver.get("http://apply.hzcb.gov.cn/apply/app/status/norm/person")
time.sleep(0.1)

qihaoEle = driver.find_element_by_id("issueNumber")
qihaoSelect = Select(qihaoEle)
all_options = qihaoSelect.options;
optStrs = []
for all_option in all_options:
    optStrs.append(all_option.text)
print optStrs
for optStr in optStrs[1:]:
    print optStr
    retry(lambda:Select(driver.find_element_by_id("issueNumber")).select_by_value(optStr))
    retry(lambda:driver.find_element_by_xpath('//*[@id="search"]').click())
    retry(lambda:driver.find_element_by_class_name("totalcount").text)
    total = int(driver.find_element_by_class_name("totalcount").text)
    d = {}
    lastText = ""
    while True:
        try:
            # 找出当前页的所有名字
            trEles = driver.find_elements_by_class_name("content_data") + driver.find_elements_by_class_name("content_data1");
            for trEle in trEles:
                tdEles = trEle.find_elements_by_tag_name("td");
                d[tdEles[0].text] = tdEles[1].text
            # 点击下一页
            try:
                nextEles = driver.find_elements_by_class_name("taiji_pager_item");
                nextEle = None;
                for ele in nextEles:
                    if ele.text.strip() == ">":
                        nextEle = ele
                        break;
                if nextEle:
                    curPage = nextEle.get_attribute("value")
                    nextEle.click();
                    print "[%s] total[%s] current[%s] page[%s]"%(optStr, total, len(d), curPage)
                    if lastText == curPage:
                        break;
                    else:
                        lastText = curPage
                else:
                    break
            except Exception, e:
                print e
                import traceback
                print traceback.format_exc();
                if len(d) < total:
                    pass
                else:
                    break
        except:
            time.sleep(0.1)
    
    resultDate = [[], []]
    for key in d:
        resultDate[0].append(key);
        resultDate[1].append(d[key]);
    writeExcel(resultDate, "yaohao/yaohao_"+optStr+".xls");
driver.quit()

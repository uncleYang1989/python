#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
from com.office.baike.FlowInfo import FlowInfo
forbidCodeErr()

from com.office.util.fileUtil import appendFile
fi = FlowInfo("baike.ini")
fi.driver.get("http://baike.baidu.com/")
for key in fi.keys:
    print key
    if key in fi.keyStr:
        print key, "之前处理过了，这次直接跳过"
        continue
    try:
        fi.driver.find_element_by_id("query").clear();
        fi.driver.find_element_by_id("query").send_keys(key);
        fi.driver.find_element_by_id("search").click();
        mainContentEle = fi.driver.find_element_by_class_name("main-content")
        divEles = mainContentEle.find_elements_by_tag_name("div");
        for i in range(len(divEles)):
            divEle = divEles[i];
            if u"歌诀"==divEle.text:
                print divEles[i+1].text + "\n"
                appendFile(fi.reusltPathname, divEles[i+1].text + "\n")
                print divEles[i+1].text
                break;
        #记录已经执行的关键字
        appendFile(fi.recordPathname, key.decode('utf8').encode("gbk") + "\n")
    except Exception,e:
        print e
    #记录已经执行的关键字
fi.driver.quit()

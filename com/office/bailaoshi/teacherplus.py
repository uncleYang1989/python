#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
import time, re
forbidCodeErr()
# #使用第三方库，模拟浏览器登录
from selenium import webdriver
driver = webdriver.Firefox()
username = "wys_kmj"
password = "123456"
driver.get("http://www.teacherplus.cn/Members/Login");
driver.find_element_by_xpath('//*[@id="content"]/div/form/div[1]/div[1]/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="content"]/div/form/div[1]/div[2]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="content"]/div/form/div[1]/div[3]/button').click();
time.sleep(1)
driver.find_element_by_xpath('//*[@id="learingtipbox"]/div/div/div[1]/button/span').click();
time.sleep(1)

itemEles = driver.find_elements_by_class_name("course-item-info");
taskUrls = [];
for itemEle in itemEles:
    process = itemEle.find_element_by_class_name("progress-bar-success").get_attribute("style")
    process = re.findall(r"\d+\.?\d*",process)[0]
    if process != 100:
        taskUrls.append(itemEle.find_element_by_class_name("btnPrepare").get_attribute("href"))
print "task size",len(taskUrls)
costAll = 0
movieUrls = [];
for taskUrl in taskUrls:
    driver.get(taskUrl);
    taskEles = driver.find_elements_by_class_name("task");
    for taskEle in taskEles:
        if -1 == taskEle.get_attribute("class").find("complete"):
            if taskEle.find_element_by_class_name("text-muted").text.strip():
                cost = int(taskEle.find_element_by_class_name("text-muted").text.strip().split(r":")[0]) + 3
                movieUrl = taskEle.find_element_by_class_name("task-todo").get_attribute("href");
                movieUrls.append([cost, movieUrl]);
    
for cost, movieUrl in movieUrls:
    costAll += cost;
for cost, movieUrl in movieUrls:
    print u"大概还需要",costAll,u"分钟.."
    print u"现在开始播放", movieUrl
    print u"预计用时", cost ,u"分钟"
    driver.get(movieUrl);
    driver.find_element_by_xpath('//*[@id="example_video_1"]/div[5]').click();
    time.sleep(cost*60);
    costAll -= cost;
#         overtime = cost * 2 * 60 + time.time();
#         while time.time() < overtime:
#             time.sleep(1);
#             videoStateEles = driver.find_elements_by_class_name("videostateprog");
#             for videoStateEle in videoStateEles:
#                 if re.findall(r"\d+\.?\d*",videoStateEle.get_attribute("style"))[0] != 100:
#                     continue;
#             break;
driver.quit()
#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年4月21日

@author: yangjie
'''
import time, re
# #使用第三方库，模拟浏览器登录
from selenium import webdriver
driver = webdriver.Firefox()
while True:
    username = "wys_kmj"
    password = "123456"
    driver.get("http://www.teacherplus.cn/Members/Login");
    driver.find_element_by_xpath('//*[@id="content"]/div/form/div[1]/div[1]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="content"]/div/form/div[1]/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="content"]/div/form/div[1]/div[3]/button').click();
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="learingtipbox"]/div/div/div[1]/button/span').click();
        time.sleep(1)
    except:
        pass
    
    itemEles = driver.find_elements_by_class_name("course-item-info");
    taskUrls = [];
    for itemEle in itemEles:
        process = itemEle.find_element_by_class_name("progress-bar-success").get_attribute("style")
        process = re.findall(r"\d+\.?\d*",process)[0]
        if process != u"100":
            taskUrls.append(itemEle.find_element_by_class_name("btnPrepare").get_attribute("href"))
    print "task size",len(taskUrls)
    if len(taskUrls) <= 0:
        break;
    costAll = 0
    movieUrls = [];
    for taskUrl in taskUrls:
        driver.get(taskUrl);
        taskEles = driver.find_elements_by_class_name("task");
        for taskEle in taskEles:
            if -1 == taskEle.get_attribute("class").find("complete"):
                if taskEle.find_element_by_class_name("text-muted").text.strip():
                    tmpTime = taskEle.find_element_by_class_name("text-muted").text.strip().split(r":")
                    cost = float(tmpTime[0]) + float(tmpTime[1])/60.0
                    movieUrl = taskEle.find_element_by_class_name("task-todo").get_attribute("href");
                    movieUrls.append([cost, movieUrl]);
        
    for cost, movieUrl in movieUrls:
        costAll += cost;
    print "movie size", len(movieUrls)
    if len(movieUrls) <= 0:
        break;
    for cost, movieUrl in movieUrls:
        print u"大概还需要",costAll,u"分钟.."
        print u"现在开始播放", movieUrl
        costAll -= cost;
        driver.get(movieUrl);
        driver.find_element_by_xpath('//*[@id="example_video_1"]/div[5]').click();
        try:
            videoStateEles = driver.find_elements_by_class_name("videostateprog");
            completeSize = 0;
            for videoStateEle in videoStateEles:
                if re.findall(r"\d+\.?\d*",videoStateEle.get_attribute("style"))[0] == u"100":
                    completeSize += 1;
                else:
                    videoStateEle.click();
                    break;
            cost = (1 - (completeSize/float(len(videoStateEles)))) * cost
        except Exception, e:
            print e
        print u"预计用时", cost ,u"分钟"
        sleepNum = cost*60 + 30;
        while sleepNum > 0:
            sleepNum = sleepNum - 1;
            time.sleep(1);
            try:
                driver.execute_async_script(u"$('title').text('%d秒后进入下一段视频,总共还需%d分钟.')"%(sleepNum, costAll))
            except:
                pass
        break;
driver.quit()
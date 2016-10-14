#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
subp=subprocess.Popen('python /Users/yangjie/mywork/icode/cloudnms/sky-auto/AutoBuildSystem/ndbs/build.py  master_3.5.0 Cloud 1',shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print u"\n========日志========\n"
while subp.poll() == None:
    print subp.stdout.readline(),
print u"\n========错误========\n"
for s in  subp.stderr.readlines():
    print s,
print u"\n========退出码========\n"
print subp.returncode


# from selenium import webdriver
# executable_path="/Users/yangjie/Documents/env/python/chromedriver_2.21/chromedriver_mac32/chromedriver"
# browser = webdriver.Chrome(executable_path=executable_path)
# 
# browser.get("http://music.163.com/#/album?id=145852")
# browser.switch_to_frame('g_iframe')
# print u'专辑名字：', browser.find_element_by_class_name('f-ff2').text
# for each in browser.find_elements_by_css_selector('a[href^=\/song]'):
#     print u"歌曲名字：",each.text
# browser.quit()
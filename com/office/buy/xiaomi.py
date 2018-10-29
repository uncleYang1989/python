#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2012年4月27日

@author: yangjie
'''
from com.office.util.codeUtil import forbidCodeErr
import time
from com.office.util.pubUtil import retry
forbidCodeErr()
# #使用第三方库，模拟浏览器登录
from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/jyang/work/env/py/selenium/chromedriver")
driver.get("https://www.mi.com/index.html");
while True:
    try:
        if r"item.mi.com/product" in driver.current_url:
            driver.find_element_by_link_text(u"加入购物车").click();
        elif r"static.mi.com/buySuccess" in driver.current_url:
            driver.find_element_by_link_text(u"去购物车结算").click();
        elif r"static.mi.com/cart/" in driver.current_url:
            driver.find_element_by_link_text(u"去结算").click();
        elif r"order.mi.com/buy/checkout" in driver.current_url:
            retry(lambda:driver.find_element_by_class_name("J_addressItem").click(), raiseOnError = True);
            retry(lambda:driver.find_element_by_link_text(u"立即下单").click(), raiseOnError = True);
            break
    except:
        time.sleep(0.01)
        continue


#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/9/1 9:17
     @Author  : wsh_oo
     @File    : zhimadaili.py
     @Software: PyCharm
'''
from selenium import webdriver
import ssl
import time, os
from configparser import ConfigParser

cf=ConfigParser()
ini_path = os.path.join(os.path.dirname(__file__),'data.ini')
print(ini_path)
cf.read(ini_path)
user = cf.get('data','user')
passwd = cf.get('data','passwd')

ssl._create_default_https_context = ssl._create_unverified_context # SSL Error

options = webdriver.ChromeOptions()
options.add_argument('headless')
drive = webdriver.Chrome()# (chrome_options=options)

drive.get("http://h.zhimaruanjian.com/")
time.sleep(1)
drive.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/a[1]').click()

drive.find_element_by_xpath('//*[@id="login_phone"]').send_keys(user)
drive.find_element_by_xpath('//*[@id="login_password"]').send_keys(passwd)
drive.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(2)
if drive.title == "我的芝麻HTTP代理":
    print("ok")
    drive.find_element_by_xpath('//*[@id="get_free_day_package"]').click()
else:
    print("领取失败")
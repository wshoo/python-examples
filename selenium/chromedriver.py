#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 17:08
# @Author  : wsh_oo
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from selenium import webdriver
import ssl


ssl._create_default_https_context = ssl._create_unverified_context # SSL Error


browser = webdriver.Chrome()
browser.get('http://www.baidu.com')  # 打开网址

js = 'window.open("http://www.google.com");'
browser.execute_script(js)  # 新建标签页

handles = browser.window_handles  # 返回列表
for handle in handles:
    if handle != browser.current_window_handle:
        browser.switch_to.window(handle)  # 切换

browser.find_element_by_xpath('//*[@id="lst-ib"]').clear()
browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('wiki')
browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
browser.save_screenshot('page.png')  # 截屏
browser.close
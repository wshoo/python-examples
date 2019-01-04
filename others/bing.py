#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/7/30 10:38
     @Author  : wsh_oo
     @File    : bing.py
     @Software: PyCharm
'''

from urllib.request import urlretrieve,Request,urlopen
import json
import os


path = r'E:\bing'
os.makedirs(path, exist_ok=True)

url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
header = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
req = Request(url, headers=header)
response = urlopen(req).read()
date = json.loads(response)  # 转换为dict
image_url = 'https://cn.bing.com{}'.format(date['images'][0]['url'])
file_name = path+'/'+ str(date['images'][0]['enddate'])+'.jpg'
urlretrieve(image_url, filename=file_name)
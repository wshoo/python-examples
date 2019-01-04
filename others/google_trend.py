#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/11/24 14:00
     @Author  : wsh_oo
     @File    : google_trend.py.py
     @Software: PyCharm
'''
from urllib.request import Request,urlopen
import urllib
url_dict = {
    "hl" : "zh-CN",
    "tz" : "-480",
    "req" : "{'comparisonItem':[{'keyword':'nokia'','geo':'US'','time':'today+12-m'}]','category':0','property':''}',",
    "tz" : "-480"
}
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}
data = urllib.parse.urlencode(url_dict).encode('utf-8')
data = bytes(data)
url='https://trends.google.com/trends/api/explore'
req = Request(url,data,headers=header,allow_redirects=False)
response = urlopen(req).read()
print("getting page...")
print(response.decode('utf-8'))
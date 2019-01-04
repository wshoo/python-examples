#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
----------------------------------------------
         @File       :  Request_.py           
         @Description:                       
         @Author     :  wsh_oo               
         @Time       :  18-5-27 下午1:35      
         @Software   :  PyCharm      
----------------------------------------------
"""
from urllib.request import Request,urlopen
from urllib.parse import urlencode
if __name__ == '__main__':

    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    dict = {
        'name': 'Germey'
    }
    data = bytes(urlencode(dict), encoding='utf8') # 传入类型为 bytes（字节流）
    req = Request(url=url, data=data, headers=headers, method='POST')
    response = urlopen(req)
    print(response.read().decode('utf-8'))

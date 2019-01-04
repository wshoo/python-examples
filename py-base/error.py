#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
----------------------------------------------
         @File       :  error.py           
         @Description:                       
         @Author     :  wsh_oo               
         @Time       :  18-5-29 上午9:22      
         @Software   :  PyCharm      
----------------------------------------------
"""

from urllib import request, error

try:
    response = request.urlopen('http://www.baidu.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('request successfully')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
----------------------------------------------
         @File       :  timeout.py           
         @Description:                       
         @Author     :  wsh_oo               
         @Time       :  18-5-27 下午1:15      
         @Software   :  PyCharm      
----------------------------------------------
"""
import socket
from urllib.request import urlopen
from urllib.error import URLError


if __name__ == '__main__':
    try:
        response = urlopen('http://httpbin.org/get', timeout=0.1)
    except URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('time out')

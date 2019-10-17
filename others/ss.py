#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
----------------------------------------------
         @File       :  1.py
         @Description:
         @Author     :  wsh_oo
         @Time       :  18-5-27 上午10:21
         @Software   :  PyCharm
----------------------------------------------
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import os
import re
import base64
from bs4 import BeautifulSoup as bs
import pyperclip


def get_content(link):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = Request(link, headers=headers)
    try:
        content = urlopen(req)
        return content
    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.reason)


def save_file(url):
    html = get_content(url)
    bs_obj = bs(html, 'lxml')
    tb = bs_obj.find_all('tr')[1:-7]
    pattern = r'</?(.+?)>'
    ss_all = ''
    for tr in tb:

        li = re.sub(pattern, '', str(tr))
        li = li.splitlines()
        # print(li)
        ss_data = '{method}:{password}@{ip}:{port}'.format(method=li[4],password=li[3],ip=li[1],port=li[2])
        form_data = str(base64.b64encode(ss_data.encode('utf-8')), 'utf-8')
        ss = 'ss://{}\n'.format(form_data)
        ss_all += ss
    print(ss_all)
    pyperclip.copy(ss_all)



if __name__ == '__main__':

    url = 'https://www.youneed.win/free-ss/comment-page-1#comments'
    save_file(url)

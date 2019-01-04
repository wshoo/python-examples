#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
----------------------------------------------
         @File       :  today_history.py
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
from bs4 import BeautifulSoup as bs


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
    txts = bs_obj.find_all('div', class_='t')

    for txt in txts:
        try:
            pattern = re.compile(r'(http:.{10,90}html)')
            link = pattern.findall(str(txt))[0]
            with open('data/'+'{}.txt'.format(txt.get_text()[6:10]), 'a') as f:
                f.write('[{}]'.format(txts.index(txt))+'\n')
                f.write('时间：'+txt.get_text()[0:10].strip()+'\n')
                f.write('标题：'+txt.get_text()[11:].strip()+'\n')
                f.write('详情：'+link+'\n')  # unknow problem
                f.write('-----------------------------------------'+'\n')
        except:
            continue


if __name__ == '__main__':
    if os.path.exists('data'):
        pass
    else:
        os.mkdir('data')
    url = 'http://www.todayonhistory.com/'
    save_file(url)

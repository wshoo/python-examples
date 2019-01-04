#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
         @Time     :  18-5-27 上午10:13
         @Author   :  wsh_oo
         @File     :  download_imag.py
         @Software :  PyCharm
'''

from urllib.request import urlopen, urlretrieve, Request
from urllib.error import HTTPError, URLError
import json
import os
from bs4 import BeautifulSoup as bs


def get_content(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = Request(url, headers=headers)
    try:
        content = urlopen(req)

    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.reason)
    return content

def get_image(url):

    base_url = 'https://cn.bing.com'
    html = get_content(url)
    my_dict = json.load(html)
    end_url = my_dict['images'][0]['url']
    print(base_url + end_url)
    image_url = base_url + end_url
    with open('url.txt', 'a') as f:
        f.write(image_url+'\n')
    image_name = end_url[16:]
    urlretrieve(image_url, 'paper/{}'.format(image_name))
    return None


def get_comnom(url):

    html = get_content(url)
    bs_obj = bs(html, 'lxml')
    text = bs_obj.find_all(id="hplaSnippet")[0].get_text()
    print(text)
    text_name = text[-5:-1]
    with open('text/'+'{}.txt'.format(text_name), 'w') as f:
        f.write(text)
    return None


if __name__ == "__main__":

    if os.path.exists('paper'):
        pass
    else:
        os.mkdir('paper')
    if os.path.exists('text'):
        pass
    else:
        os.mkdir('text')

    common_url = 'https://cn.bing.com/cnhp/life'
    json_url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    my_headers = ['Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36']
    get_image(json_url)
    get_comnom(common_url)


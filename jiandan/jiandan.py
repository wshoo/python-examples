#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2019/1/4 17:00
     @Author  : wsh_oo
     @File    : test.py
     @Software: PyCharm
'''
from urllib.request import urlretrieve, build_opener, install_opener
import requests
import threading
from lxml import etree
import time
import os
import base64

myheaders = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}


class MyThread(threading.Thread):

    def __init__(self,url,dir):
        super(MyThread, self).__init__()
        self.url = url
        self.dir = dir

    def run(self):
        os.makedirs('./{}'.format(self.dir), exist_ok=True)
        download_img(self.url, self.dir)

def download_img(url,dir):

    name = url.split("/")[-1]
    path = "{0}/{1}".format(str(dir),name)
    urlretrieve(url, path)

def get_imgurl(url):

    threads = []
    response = requests.get(url, headers=myheaders)
    html = etree.HTML(response.text)
    img_url = html.xpath("//ol[@class='commentlist']//div[@class='text']//span[@class='img-hash']")
    for url in img_url:
        url = url.text
        url = str(base64.b64decode(url), encoding = "utf-8").replace('//','http://')
        print(url)
        thread = MyThread(url,url[0:3])
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()




if __name__ == "__main__":

    before = time.time()
    for i in range(1,44):
        print('下载第{}页。。。'.format(i))
        url = "http://jandan.net/ooxx/page-{}#comments".format(i)

        get_imgurl(url)
    print('下载完成')
    spend_time = time.time()-before
    print(spend_time)
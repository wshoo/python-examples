#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/11/20 9:38
     @Author  : wsh_oo
     @File    : nfl.py
     @Software: PyCharm
'''
import re
import requests
from urllib.request import urlretrieve, build_opener, install_opener, quote
import ssl


ssl._create_default_https_context = ssl._create_unverified_context # SSL Error

def download_img(url):
    myheaders = [('User - Agent',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.17(KHTML, like Gecko) Version/3.1 Safari/525.17'), ]

    opener = build_opener()
    opener.addheaders = myheaders
    install_opener(opener)
    try:
        name = re.findall(r"altimages.*jpg",url)
        pic_name = name[0].replace("/", "-")

        urlretrieve(url, r"C:\Users\Administrator\Desktop\nhl\shop-nfl\shop-nfl\{}".format(pic_name))
    except Exception as e:
        print(name,e,sep="/////")
        pass

def dl(url):


    imgres = requests.get(url)
    name = re.findall(r"altimages.*jpg", url)
    pic_name = name[0].replace("/", "-")

    try:
        with open(r"C:\Users\Administrator\Desktop\jersey\nfl\TRENDING PLAYER\nfl-9-11-12-15-52\{}".format(pic_name), "wb") as f:
            f.write(imgres.content)
    except Exception as e:
        print(name,e,sep=">>>>>>")
    print("下载完毕")


if __name__ == "__main__":

    thread_list=[]
    with open("url.txt", "r") as f:
        for url in f.readlines():
            url = url.strip()
            print(url)
            dl(url)

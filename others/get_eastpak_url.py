#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/8/4 9:07
     @Author  : wsh_oo
     @File    : 1.py
     @Software: PyCharm
'''
from urllib.request import Request, urlopen
from lxml import etree
from fake_useragent import UserAgent


url = 'https://www.eastpak.com/oc-en/backpacks/shop-by/the-iconic-c7259.html?limit=all'
ua = UserAgent().random
header = {'UserAgent': ua}
req = Request(url, headers=header)
response = etree.HTML(urlopen(req).read())

goods = response.xpath('//ul[@class="product-list-mosaic-line product-list-with-sliders"]/li/div/div/a/@href')

for good in goods:
    if 'wishlist' not in good:
        print(good)


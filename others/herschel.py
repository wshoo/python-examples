#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/8/1 18:39
     @Author  : wsh_oo
     @File    : herschel.py
     @Software: PyCharm
'''
from urllib.request import Request,urlopen,urlretrieve
import os
import csv
from lxml import etree
import ssl
from fake_useragent import UserAgent

ssl._create_default_https_context = ssl._create_unverified_context  #https 证书信任问题


def parse(url):
    ua = UserAgent().random
    header = {"User-Agent": ua}
    req = Request(url, headers=header)
    response = etree.HTML(urlopen(req).read())
    goods_selector = response.xpath('//div[@class="colors-list m-y-1 indented js-colors-list pdp-colors-list sm-hide"]/ul[@class="colors-list__colors"]/li')

    color_li = []
    sku_li = []
    i = 0
    for goods in goods_selector:

        color = goods.xpath('//label/input/@data-color')[i]
        if color == None:
            break
        print(color)
        color_li.append(color)
        sku = goods.xpath('//label/input/@value')[i]
        print(sku)
        sku_li.append(sku)
        image_url = "https://herschel.com/content/dam/herschel/products/{0}/{1}_01.jpg".format(sku[:5], sku)
        urlretrieve(image_url, './img/{}.jpg'.format(sku))
        image_1 = "https://herschel.com/content/dam/herschel/products/{0}/{1}_02.jpg".format(sku[:5], sku)
        urlretrieve(image_1, './img/{}_1.jpg'.format(sku))
        image_2 = "https://herschel.com/content/dam/herschel/products/{0}/{1}_03.jpg".format(sku[:5], sku)
        urlretrieve(image_2, './img/{}_2.jpg'.format(sku))
        i += 1
    temp = list(zip(color_li, sku_li))
    print(temp)
    return temp


def save_csv(file_name,all_dict):

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)

        for item in all_dict:
            print(item)
            writer.writerow(item)


if __name__ == "__main__":

    goods_url = "https://herschel.com/shop/backpacks/harrison-backpack"
    os.makedirs('./img', exist_ok=True)
    os.makedirs('./data', exist_ok=True)
    temp = parse(goods_url)
    file = './data/1.csv'
    save_csv(file,temp)



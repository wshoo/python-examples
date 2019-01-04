#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/9/20 14:52
     @Author  : wsh_oo
     @File    : download_img.py
     @Software: PyCharm
'''
import os
from urllib.request import urlretrieve, build_opener, install_opener
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # SSL Error
def cbk(a,b,c):
    '''
    回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('{}%'.format(int(per)))

def dl_img(path_name):
    myheaders = [('User - Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.17'
                                  ' (KHTML, like Gecko) Version/3.1 Safari/525.17'), ]

    opener = build_opener()
    opener.addheaders = myheaders
    install_opener(opener)

    for dir_item in os.listdir(path_name):

        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):
            # 如果是文件夹，继续递归调用
            dl_img(full_path)
        else:

            try:
                if "jpg" in dir_item:
                    image_url = "https://media.hufworldwide.com/media/catalog/product/cache/image/e9c3970ab036de70892d86c6d221abfe/{0}/{1}/{2}".format(dir_item[0], dir_item[1], dir_item)
                    img_1 = image_url.replace('_01', '_02') # modelfront  modelback
                    print(img_1)
                    urlretrieve(img_1, full_path.replace('.jpg','_1.jpg'))# cdn挂代理会返回400

            except Exception as e:
                print(e)
                pass

if __name__ == "__main__":

    path = r"C:\Users\Administrator\Desktop\cache"
    dl_img(path)


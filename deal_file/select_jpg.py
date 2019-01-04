#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/12/4 16:27
     @Author  : wsh_oo
     @File    : select_jpg.py
     @Software: PyCharm
'''
import os
import os.path
import shutil
import time,  datetime


def copy_images(name, resource_path, result_path):
    '''
    :param name: txt中每一行的文件名
    :param resource_path: 图片所在文件夹
    :param result_path: 复制到目标文件夹
    :return: None
    '''

    for dir_item in os.listdir(resource_path):
        #从初始路径开始叠加，合并成可识别的操作路径
        print(dir_item)
        full_path = os.path.abspath(os.path.join(resource_path, dir_item))
        resultimg_path = os.path.abspath(os.path.join(result_path, dir_item))

        if os.path.isdir(full_path):    #如果是文件夹，继续递归调用
            copy_images(full_path)
        elif dir_item.endswith('.jpg'):
            if name == dir_item:
                try:
                    shutil.copyfile(full_path, resultimg_path)
                except Exception as e:
                    print(e,dir_item,seq="---")

if __name__ == "__main__":
    resource_path = r"C:\Users\Administrator\Desktop\审核站-1\4\w-clothing"
    result_path = r"C:\Users\Administrator\Desktop\cache\w-clothing"
    with open(r"C:\Users\Administrator\Desktop\cache\1.txt", "r") as f:
        for i in f.readlines():
            name = i.strip()
            copy_images(name, resource_path, result_path)
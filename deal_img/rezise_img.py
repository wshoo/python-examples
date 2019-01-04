#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 11:13
# @Author  : wsh_oo
# @Site    :
# @File    : resize_image.py
# @Software: PyCharm

import os
import cv2


def resize_image(image):

     top, bottom, left, right = (0, 0, 0, 0)  # 获取图像尺寸
     try:
         h, w, _ = image.shape
         longest_edge = max(h, w)  # 对于长宽不相等的图片，找到最长的一边
         if h < longest_edge:  # 计算短边需要增加多上像素宽度使其与长边等长
             dh = longest_edge - h
             top = dh // 2  # 整除
             bottom = dh - top
         elif w < longest_edge:
             dw = longest_edge - w
             left = dw // 2
             right = dw - left
         else:
             pass
         white = [255,255,255]  # RGB颜色
         # 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
         constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = white)
         return cv2.resize(constant, (longest_edge, longest_edge))  # 调整图像大小并返回
     except AttributeError as e:
         print('{}该图大小为0,请删除'.format(e))
         pass


def resize_images(path_name):

    for dir_item in os.listdir(path_name):
        #从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))

        if os.path.isdir(full_path):    #如果是文件夹，继续递归调用
            resize_images(full_path)
        elif dir_item.endswith('.jpg'):
            try:
                image = cv2.imread(full_path)
                image = resize_image(image)
                cv2.imwrite( os.path.split(full_path)[0]+ '/' + dir_item, image)
                print('Changing...{}...'.format(dir_item))
            except:
                print('请手动修改{}'.format(image))
                pass
        else:
            print('{},请转换为JPG格式'.format(dir_item))

def main():
    # 路径有中文会报错
    path = r"C:\Users\Administrator\Desktop\test"
    resize_images(path)
    print('done')

if __name__ == "__main__":
    main()

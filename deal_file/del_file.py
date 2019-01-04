#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 14:05
# @Author  : wsh_oo
# @Site    : 
# @File    : del_file.py
# @Software: PyCharm
import os


def remove_files(end_str,path_name):

    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):
            # 如果是文件夹，继续递归调用
            remove_files(end_str,full_path)
        elif dir_item.endswith(end_str):
            os.remove(full_path)
            print( 'del {}'.format(dir_item))


if __name__ == "__main__":
    """
    删除指定文件格式的文件
    """
    end_str = '.wdp'
    path_name = r"E:\image\konga"
    remove_files(end_str,path_name)
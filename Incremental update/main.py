# -*- coding: utf-8 -*-
'''
     @Time    : 2019/2/15 11:07
     @Author  : wsh_oo
     @File    : main.py
     @Software: PyCharm
'''
import os
import hashlib
import shutil


def md5_check(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def cp_file(origin_dir, target_dir):
    for dir_item in os.listdir(origin_dir):
        # 从初始路径开始叠加，合并成可识别的操作路径
        abs_path = os.path.abspath(os.path.join(origin_dir, dir_item))
        if os.path.isdir(abs_path):    # 如果是文件夹，继续递归调用
            cp_file(abs_path)
        else:
            old_path = abs_path
            new_path = abs_path.replace(os.path.split(abs_path)[0],target_dir)
            if os.path.isfile(new_path):
                if md5_check(old_path) != md5_check(new_path):
                    print(os.path.basename(old_path), os.path.basename(new_path), sep='-.-.->is updating to-.-.->')
                    shutil.copy(old_path, new_path)
            else:
                print('new file {}'.format(os.path.basename(old_path)))
                shutil.copy(old_path, new_path)

if __name__ == "__main__":
    origin = r"C:\Users\Administrator\Desktop\cahe\1"
    target = r"C:\Users\Administrator\Desktop\cahe\2"
    cp_file(origin, target)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 10:59
# @Author  : wsh_oo
# @Site    : 
# @File    : db_to_csv.py
# @Software: PyCharm
import os
import uuid
import sqlite3
import pandas as pd
import time


print(os.getcwd())
def db_to_xlsx(path_name):

    for dir_item in os.listdir(path_name):

        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):
            # 如果是文件夹，继续递归调用
            db_to_xlsx(full_path)
        else:
            # 文件
            if dir_item.endswith('.db3'):
                try:
                    conn=sqlite3.connect(full_path)
                    pd.read_sql("select * from Content", conn).to_csv(csv_dir+r"/line_{}.csv".format(str(uuid.uuid4())),encoding = 'utf-8')
                    print('convent {}'.format(dir_item))
                    conn.close()
                except:
                    assert 'error with {}'.format(full_path)

def csv_all(file_path):
    '''
    :param file_path: csv文件路径
    :return: 合并左右CSV文件
    '''
    file_name = "all.csv"
    for i in os.listdir(file_path):
        df = pd.read_csv(file_path+"/"+i)
        df.to_csv(file_path+"/"+file_name, encoding="utf_8", index=False, mode='a+')

    print('creat ..{}'.format(file_name))


if __name__ == '__main__':

    path = r"C:\Users\Administrator\Desktop\cahe"
    csv_dir = path+r"\csv"
    os.makedirs(csv_dir, exist_ok=True)
    db_to_xlsx(path)
    time.sleep(1)
    csv_all(csv_dir)


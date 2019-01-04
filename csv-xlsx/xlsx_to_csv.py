#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 11:13
# @Author  : wsh_oo
# @Site    : 
# @File    : xlsx_to_csv.py
# @Software: PyCharm

import os
import openpyxl
import csv


def xlsx_to_csv(path_name):
    '''
    :param path_name:
    :return: 将当前目录下的xlsx文件转化为csv,保存在当前目录
    '''
    for dir_item in os.listdir(path_name):

        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):
            xlsx_to_csv(full_path)
        elif dir_item.endswith('.xlsx'):
            wb = openpyxl.load_workbook(filename=full_path, read_only=TabError)
            sheet_name = wb.sheetnames
            sheet = wb[sheet_name[0]]
            with open(os.path.splitext(full_path)[0]+'.csv', 'w', newline='', encoding='utf-8') as fw:
                data = csv.writer(fw)
                for row in sheet.rows:
                    row = [i.value for i in row]
                    data.writerow(row)
                print('writing {}'.format(full_path))


if __name__ == '__main__':

    path = r"C:\Users\Administrator\Desktop\test"
    xlsx_to_csv(path)

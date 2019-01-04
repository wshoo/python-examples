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
import sys
import xlwings as xw

def add_title(path_name):
    '''
    将路径下xlsx文件加表头
    :param path_name:
    :return:
    '''

    for dir_item in os.listdir(path_name):

        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):
            add_title(full_path)
        elif dir_item.endswith('.xlsx'):
            app = xw.App(visible=True, add_book=False, )
            wb = xw.Book(full_path)
            sht = wb.sheets['Sheet1']  # 注意表名是否正确
            sht.api.Rows(1).Insert()
            sht.range('A1').value = ["v_sku", "v_name", "v_short_description", "v_description", "v_image", "v_url", "v_attribute", "v_price", "v_specials_price", "v_specials_expire_date", "v_date_added", "v_in_stock", "v_status", "v_viewed", "v_ordered", "v_category_sku", "v_sort_order", "v_meta_title", "v_meta_keywords", "v_meta_description", "v_brand_filter", "v_class_filter", "v_color_filter", "v_gender_filter", "v_material_filter", "v_year_filter", "v_origin_filter", "v_series_filter", "v_spec_filter"
]
            print("dealing {}".format(dir_item))
            print('ok')
            wb.save()
            wb.close()
            app.quit()


if __name__ == '__main__':

    path = r"C:\Users\Administrator\Desktop\test"
    add_title(path)
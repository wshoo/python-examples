#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 12:42
# @Author  : wsh_oo
# @Site    :
# @File    : select_from_xlsx.py
# @Software: PyCharm

import xlwings as xw


def select_line(select_file, xlsx_file):
    '''
    :param select_file: 将要查找的字段放到txt文件中
    :param xlsx_file: 要查找的Excel文件
    :return: 标记单元格颜色
    '''
    app = xw.App(visible=True, add_book=False,)
    wb = xw.Book(xlsx_file)
    sht = wb.sheets['Sheet1'] # 注意表名是否正确
    max_row = sht.range('A1').current_region.last_cell.row  # 中间不能有空行
    print(max_row)
    with open(select_file) as f:
        for line in f.readlines():
            for i in range(1,max_row+1):
                cell = 'E'+ str(i)
                if line.strip() in sht.range(cell).value:
                    sht.range(cell).color=(255,255,0) # 标记为黄色
                    # sht.range(cell).add_hyperlink(r'www.baidu.com', '百度', '提示：点击即链接到百度')
                    # sht.range(cell).api.EntireRow.Delete() # 删除整行
                    # sht.api.Rows(row_number).Insert()
                    print('done {}'.format(cell))
    print('ok')
    wb.save()
    wb.close()
    app.quit()


if __name__ == "__main__":

    # 中文路径报错
    select_file = r"C:\Users\Administrator\Desktop\bodycare\bodycares\list.txt"
    xlsx_file = r"C:\Users\Administrator\Desktop\bodycare\test.xlsx"
    select_line(select_file,xlsx_file)
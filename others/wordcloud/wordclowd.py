#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
     @Time    : 2018/9/15 14:18
     @Author  : wsh_oo
     @File    : wordclowd.py
     @Software: PyCharm
'''
import jieba
with open("./txt/1.txt", 'rb') as f:
    text = f.read()
    segs = jieba.cut(text)
cloud_text=",".join(segs)
import numpy as np
from PIL import Image
cloud_mask = np.array(Image.open("./img/1.png"))
from wordcloud import WordCloud
wc = WordCloud(
    background_color="white", #背景颜色
    mask=cloud_mask,
    max_words=500, #显示最大词数
    font_path=r"C:\Windows\Fonts\FZSTK.TTF",  #使用字体
    min_font_size=10,
    max_font_size=200,
    width=1000  #图幅宽度
    )
wc.generate(cloud_text)
wc.to_file("pic.png")
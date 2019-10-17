#-*- coding:utf-8 -*-

from urllib.request import urlretrieve, build_opener, install_opener
import ssl
import datetime

ssl._create_default_https_context = ssl._create_unverified_context # SSL Error

def download_img(url):

	myheaders = [('User - Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.17(KHTML, like Gecko) Version/3.1 Safari/525.17'), ]

	opener = build_opener()
	opener.addheaders = myheaders
	install_opener(opener)
	name = url.split("/")[-1]
	path = "./{}".format(name)
	# url = "https://whitepaper.coinspice.io/static/comic/cn/pc/{}.jpg".format(name)
	urlretrieve(url,path)

"""
with open(r"C:\Users\Administrator\Desktop\script\url.txt", "r") as f:
	
	for url in f.readlines():
		url = url.strip()
		try:
			download_img(url)
			print('downloading...{}'.format(url))
		except Exception as e:
			print(e)
			pass
"""
download_img('http://pic1.win4000.com/tj/2018-12-13/5c121da93b036.png')
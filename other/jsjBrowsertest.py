#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: 2.useBrowser.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/16 12:47
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""
import time
from selenium import webdriver


def OpenPage(url, name):
    # driver = webdriver.Firefox()
    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(2)
    filename = name + ".png"
    driver.save_screenshot("..\\images\\" + filename)
    driver.close()



class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    while True:
        id = input("请输入织轴编号：")
        print("id: ", id)
        url = "http://www.tssmax.cn/htzg/weaverdetail.html?id=" + id
        OpenPage(url, id)

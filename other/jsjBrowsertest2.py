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
from selenium.webdriver.firefox.options import Options


def OpenPage(url, name):
    # options = Options()
    # options.add_argument('-headless')
    # driver = webdriver.Firefox(firefox_options=options)
    driver = webdriver.PhantomJS()
    driver.get(url)
    while "联发" not in driver.page_source:
        time.sleep(1)
    filename = name + ".png"
    driver.save_screenshot("..\\images\\" + filename)
    driver.close()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    id = input("请输入织轴编号：")
    print("id: ", id)
    url = "http://www.tssmax.cn/htzg/weaverdetail.html?id=" + id
    OpenPage(url, id)

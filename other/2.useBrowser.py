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


def OpenPage(url, name):
    from selenium import webdriver
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.save_screenshot("image" + str(name) + ".png")


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    url = "http://image.baidu.com/"
    OpenPage(url, 1)

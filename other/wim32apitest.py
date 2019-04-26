#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: wim32apitest.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/06 11:24
@description:This file is fro ...  
"""
import win32api
import _thread
import time


def show(num):
    temp = win32api.MessageBox(0, "你的QQ存在安全隐患%d！" % num, "TIPs", 0)
    print("temp%d =" % num, temp)


class Main:
    def __init__(self):
        pass


if __name__ == "__main__":
    for i in range(5):
        _thread.start_new_thread(show, (i,))
    time.sleep(20)

#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: winprocess.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/07 10:20
@description:This file is fro 队列收集数据
"""

import multiprocessing
import os


def func(myque, i):
    myque.put([os.getpid(), "123456789", i])
    print(os.getpid(), os.getppid())


class Main():
    def __init__(self):
        pass


que = multiprocessing.Queue()
mylist = []
if __name__ == "__main__":
    for i in range(10):
        process1 = multiprocessing.Process(target=func, args=(que, i))
        mylist.append(process1)
        process1.start()
        print(que.get())
    for i in mylist:
        i.join()

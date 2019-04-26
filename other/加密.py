#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: 加密.py
@version: v1.0 
@author: WeWe 
@time: 2018/05/17 17:10
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import hashlib


def func():
    pass


class Other():
    def __init__(self):
        pass


def main():
    mingstr = input("请输入加密字符串:")
    m = hashlib.sha1()
    m.update(mingstr.encode("utf-8"))
    minstr = m.hexdigest()
    print(minstr)


if __name__ == "__main__":
    main()
    pass

#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: codetest.py
@version: v1.0 
@author: WeWe 
@time: 2018/10/24 10:36
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""


def str_to_utf8():
    id_str = "编码测试"  # 1501020800061803170020
    id_code = id_str.encode("utf-8")
    print(id_code)


class Other(object):
    def __init__(self):
        pass


def main():
    str_to_utf8()
    pass


if __name__ == "__main__":
    main()
    pass

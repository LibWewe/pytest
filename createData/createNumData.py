#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: createNumData.py
@version: v1.0 
@author: WeWe 
@time: 2019/04/11 17:29
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import random


def create(n):
    data_list = []
    for i in range(n):
        data = random.randint(0, 1000000)
        data_list.append(data)
    return data_list


class Other(object):
    def __init__(self):
        pass


def main():
    for i in range(9000):
        data_list = create(1000)
        with open("num.data", "a+") as f:
            for data in range(len(data_list)):
                f.write(str(data_list[data]))
                f.write(" ")
            f.write("\n")
        # print(data_list)


if __name__ == "__main__":
    main()
    pass

#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: struct_test.py
@version: v1.0 
@author: WeWe 
@time: 2018/11/21 9:23
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro 测试结构体的使用方法
"""

import struct
import ctypes


class struct_test(ctypes.Structure):
    _fields_ = [
        ("buffLen", ctypes.c_uint32),
        ("t_name1", ctypes.c_char * 20),
        ("temperature1", ctypes.c_uint32),
        ("t_name2", ctypes.c_char * 20),
        ("temperature2", ctypes.c_uint32),
        ("p_name1", ctypes.c_char * 20),
        ("pressure1", ctypes.c_uint32),
        ("p_name2", ctypes.c_char * 20),
        ("pressure2", ctypes.c_uint32),
    ]


def main():
    try:
        buf_strut = struct_test(171, b'temperature1', 200, b'temperature2', 300, b'pressure1', 400, b'pressure2', 500)
        buf = struct.pack('I20sI20sI20sI20sI', buf_strut.buffLen, buf_strut.t_name1, buf_strut.temperature1,
                          buf_strut.t_name2,
                          buf_strut.temperature2, buf_strut.p_name1, buf_strut.pressure1, buf_strut.p_name2,
                          buf_strut.pressure2)
    except Exception as e:
        print(e)
    resp = struct.unpack('I20sI20sI20sI20sI', buf)
    for i in resp:
        if isinstance(i, int):
            print(i)
        else:
            print(i.decode("ascii"))


if __name__ == "__main__":
    main()
    pass

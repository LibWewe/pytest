#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: FeiQitest.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/06 8:52
@description:This file is fro ...  
"""

import socket

def func():
    pass


class Main:
    def __init__(self):
        pass


if __name__ == "__main__":
    mystr = "1_lbt4_10#32899#002481627512#0#0#0:1289671407:你的baby:你的hello:288:"
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.connect(("192.168.0.102", 2425))
    while True:
        inputstr = input(">>")
        if inputstr == "quit":
            break
        sendstr = mystr + inputstr
        udp.send(sendstr.encode("gbk"))

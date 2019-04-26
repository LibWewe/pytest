#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: tcp_http.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/08 14:04
@description:This file is fro ...  
"""

import socket

sendstr = """GET https://127.0.0.1:8000/index/ HTTP/1.1
    Host: www.baidu.com
    Connection: keep-alive
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
    Accept-Language: zh-CN,zh;q=0.8
    """

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('119.75.217.109', 80))
    s.connect(('127.0.0.1', 8000))
    print("connect.....")
    s.send(sendstr.encode("utf-8"))
    print("send....")
    buf = s.recv(1024)
    print("recv....")
    i = 0
    while len(buf):
        print(buf.decode("gbk"))
        buf = s.recv(1024)
        i += 1

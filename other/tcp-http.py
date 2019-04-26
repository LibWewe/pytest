#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: tcp-http.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/08 13:20
@description:This file is fro ...  
"""
import socket

get_str = r'GET / HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\nAccept: */*\r\n\r\n'
post_str = r'POST %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\n\r\n%s\r\n\r\n'


def get(url, port):
    sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_fd.connect((url, port))
    sock_fd.send((get_str % url).encode("utf-8"))

    response = ''
    temp = sock_fd.recv(4096)
    print(temp.decode("utf-8"))
    while temp:
        temp = sock_fd.recv(4096)
        print(temp.decode("utf-8"))
        response += temp

    return response


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    result = get("127.0.0.1", 8000)
    print(result)

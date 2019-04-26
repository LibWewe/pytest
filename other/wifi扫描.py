#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: wifi扫描.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/07 15:31
@description:This file is fro ...  
"""

import time
import logging
import pywifi

pywifi.set_loglevel(logging.INFO)


def go_scan():
    wifi = pywifi.PyWiFi()  # 初始化wifi

    iface = wifi.interfaces()[0]  # 第一个无线网卡，
    iface.scan()  # 扫描
    time.sleep(5)
    bsses = iface.scan_results()  # 扫描结果
    for data in bsses:  # wifi创建一个对象
        print(data.ssid)


if __name__ == "__main__":
    go_scan()

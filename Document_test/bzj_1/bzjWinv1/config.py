#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: config.py
@version: v1.0 
@author: WeWe 
@time: 2018/07/18 11:33
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import os

BASE_DIRS = os.path.dirname(__file__)

# 数据库配置
mysql = {
    "host": "localhost",
    "user": "root",
    "passwd": "mysql20180223%",
    "dbName": "bzj1"
}

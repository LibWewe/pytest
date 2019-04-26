#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: jsjtest.py
@version: v1.0 
@author: WeWe 
@time: 2018/06/21 9:36
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import urllib.request
import urllib.parse
import json


def func():
    pass


class Other():
    def __init__(self):
        pass


weaverCardListInfo = {
    "pageNo": 1,
    "pageSize": 10,
    "machineId": "M0010",
}
weaverCardListInfoJson_str = json.dumps(weaverCardListInfo)
loginInfo = {
    "account": "jslfscz",
    "password": "123456"
}

loginInfoJson_str = json.dumps(loginInfo).encode("utf-8")


# loginInfoJson_str = urllib.parse.urlencode(loginInfo).encode("utf-8")


def main():
    headerstr = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    # url1 = 'http://www.baidu.com/'
    url1 = 'http://47.94.84.139:82/login'
    req = urllib.request.Request(url=url1, headers=headerstr, data=loginInfoJson_str)
    # req = urllib.request.Request(url=url1, headers=headerstr)
    res = urllib.request.urlopen(req)  # .read().decode("utf-8")

    print(json.load(res))


if __name__ == "__main__":
    main()
    pass

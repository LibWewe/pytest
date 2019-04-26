#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: 1neihanduanzi.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/15 9:53
@lib v: Python 2.7.14
@description:This file is fro 爬去内涵段子网页中的段子
"""
import re
import urllib2


class MySpider:
    def __init__(self):
        """
            初始化变量
        """
        self.page = 1
        pass

    def LoadPage(self, page):
        """
            下载页面数据
        """
        # 设计url
        url = r"http://www.neihanpa.com/article/list_5_" + str(page) + ".html"
        # 设计数据请求头
        header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        # 创建一个请求对象
        request = urllib2.Request(url, headers=header)
        # 获取页面返回对象
        response = urllib2.urlopen(request)
        # 获取html页面全部字符串
        html = response.read()
        print(html.decode("gbk"))
        # 创建正则表达式
        parttern = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
        # 获取列表数据
        datalist = parttern.findall(html)
        print("----------------------------------------------------------------------------------------------------")
        print(datalist)
        for i in datalist:
            print(i.decode("gbk"))

    def DealData(self):
        """
            数据处理
        """
        pass

    def WriteData(self):
        """
            将数据写入文件
        :return:
        """
        pass

    def StartWork(self):
        """
            爬虫调度器
        :return:
        """
        pass


if __name__ == "__main__":
    nhspider=MySpider()
    nhspider.LoadPage(1)

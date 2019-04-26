#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: data_read.py
@version: v1.0 
@author: WeWe 
@time: 2018/10/24 14:53
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import pprint


def load_json():
    """
    处理json文件
    :return:
    """
    import json
    try:
        json_data = open("config.json").read()
        data = json.loads(json_data)
    except Exception as e:
        print(e)
    print("data type:", type(data))
    print("data[0] type", type(data[0]))
    for item in data[0]:
        print(data[0][item])
    if "s2_port" in data[0]:
        print(data[0]["s2_port"])
    else:
        print("has none")


def main1():
    load_json()


def load_xml1():
    """
    第1种方式解析XML文件，根据标签名解析xml
    :return:
    """
    import xml.dom.minidom as xmldom
    cfg_obj = xmldom.parse("config.xml")
    cfg_ele_obj = cfg_obj.documentElement
    # 读取mysql数据库相关配置
    cfg_sql_ele_obj = cfg_ele_obj.getElementsByTagName("sqlcfg")
    host = cfg_sql_ele_obj[0].getElementsByTagName("mysql_host")
    print("mysql_host:", host[0].childNodes[0].data)
    user = cfg_sql_ele_obj[0].getElementsByTagName("mysql_user")
    print("mysql_user:", user[0].childNodes[0].data)
    pwd = cfg_sql_ele_obj[0].getElementsByTagName("mysql_pwd")
    print("mysql_pwd:", pwd[0].childNodes[0].data)
    db_name = cfg_sql_ele_obj[0].getElementsByTagName("dbName")
    print("dbName:", db_name[0].childNodes[0].data)

    # 读取网线扫描枪配置参数
    cfg_scanner_ele_obj = cfg_ele_obj.getElementsByTagName("scanner")
    s1_ip = cfg_scanner_ele_obj[0].getElementsByTagName("s1_ip")
    print("s1_ip:", s1_ip[0].childNodes[0].data)
    s1_port = cfg_scanner_ele_obj[0].getElementsByTagName("s1_port")
    print("s1_port:", s1_port[0].childNodes[0].data)
    s2_ip = cfg_scanner_ele_obj[0].getElementsByTagName("s2_ip")
    print("s2_ip:", s2_ip[0].childNodes[0].data)
    s2_port = cfg_scanner_ele_obj[0].getElementsByTagName("s2_port")
    print("s2_port:", s2_port[0].childNodes[0].data)


def load_xml2():
    """
    第2种方式解析xml，进行轮询
    :return:
    """
    from xml.etree import ElementTree as ET
    tree = ET.parse("config.xml")
    root = tree.getroot()
    root_len = len(root)
    for i in range(root_len):
        print("\n" + 30 * "*")
        print(root[i].tag)
        child_len = len(root[i])
        for j in range(child_len):
            print(root[i][j].tag, ":", root[i][j].text)


def main2():
    load_xml1()


class Other(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    main2()
    pass

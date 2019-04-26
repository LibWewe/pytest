#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: xmlTest.py
@version: v1.0 
@author: WeWe 
@time: 2019/03/13 17:10
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""
from xml.dom.minidom import parse


def xml_test():
    cfg_list = {"sql_cfg": [{"mysql_host": ""},
                            {"mysql_user": ""},
                            {"mysql_pwd": ""},
                            {"dbName": ""}],
                "scanner": [{"s1_ip": ""},
                            {"s1_port": ""},
                            {"s2_ip": ""},
                            {"s2_port": ""}],
                "level": [{"msg_level": ""}],
                "sel": [{"selComPort": ""},
                        {"selBaudRate": ""}]}

    config_tree = parse("config.xml")
    c = config_tree.documentElement
    for cfg in cfg_list:
        sql = c.getElementsByTagName(cfg)[0]
        i = 0
        for item in cfg_list[cfg]:
            tmp_item = sql.getElementsByTagName(sorted(item.keys())[0])[0]
            data = tmp_item.childNodes[0].data
            cfg_list[cfg][i][sorted(item.keys())[0]] = data
            i += 1
    print(cfg_list)


def main():
    xml_test()


if __name__ == "__main__":
    main()
    pass

#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: test1.py
@version: v1.0 
@author: WeWe 
@time: 2018/07/19 16:04
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

from bzjWinv1.config import mysql
import pymysql
import random
import time
from hashlib import sha1


class test1():
    """
    SELECT COUNT(*) FROM tableName WHERE exceptions  查询表中满足条件的数据的数量
    SELECT * FROM tableName ORDER BY id DESC LIMIT 0,10 查询表中id 最大的10条数据
    """

    def __init__(self):
        self.db = pymysql.Connect(mysql["host"], mysql["user"], mysql["passwd"], mysql["dbName"])
        self.cursor = self.db.cursor()

    def insertDateGZL(self):
        for i in range(0, 155):
            gongzilunid = "GZL" + str(i)
            zhongliang = random.uniform(500, 800)
            chengzhongtime = str(round(time.time() * 1000))
            time.sleep(0.01)
            isNum = int(random.uniform(0, 1000))
            shifoucheng2 = isNum % 2
            if shifoucheng2 == 1:
                zhongliang2 = random.uniform(500, 800)
                chengzhongtime2 = str(round(time.time() * 1000))
            else:
                zhongliang2 = 0
                chengzhongtime2 = ""
            sqlStr = "INSERT INTO gongzilun (gongzilunid,zhongliang,chengzhongtime,shifoucheng2,zhongliang2,chengzhongtime2) " \
                     "VALUES ('%s','%f','%s','%d','%f','%s')" % (
                         gongzilunid, zhongliang, chengzhongtime, shifoucheng2, zhongliang2, chengzhongtime2)
            try:
                self.cursor.execute(sqlStr)
                self.db.commit()
            except Exception as e:
                print(e)
                return
        print("INSERT success")

    def clearDateGZL(self):
        sqlStr = "DELETE FROM gongzilun WHERE id > 0"
        try:
            self.cursor.execute(sqlStr)
            self.db.commit()
        except Exception as e:
            print(e)
            return
        print("clear success")

    def clearLineuser(self):
        sqlStr = "DELETE FROM lineuser WHERE uname = 'admin' OR uname = 'user'"
        try:
            self.cursor.execute(sqlStr)
            self.db.commit()
        except Exception as e:
            print(e)
            return
        print("clear success")

    def changepwd(self):
        uname = "admin"
        s1 = sha1("123456".encode("utf-8"))
        upwd = s1.hexdigest()
        # sqlStr = "UPDATE adminuser SET uname = '{0}',upwd = '{1}' WHERE id = 1".format(uname, upwd)
        # sqlStr = "UPDATE login SET upwd = '{0}' WHERE uname = 'admin'".format(upwd)
        sqlStr = "UPDATE login SET upwd = '{0}' WHERE uname = 'user'".format(upwd)
        print(sqlStr)
        try:
            self.cursor.execute(sqlStr)
            self.db.commit()
        except Exception as e:
            print(e)
            return
        print("change success")

def main():
    T = test1()
    # T.insertDateGZL()
    # T.clearDateGZL()
    # T.clearLineuser()
    T.changepwd()


if __name__ == "__main__":
    main()
    pass

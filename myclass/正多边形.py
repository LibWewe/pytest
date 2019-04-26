#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: 正多边形.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/01 17:20
@description:This file is fro ...  
"""

import math


def func():
    pass


class RegularPoylgon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def setN(self, n):
        self.__n = n

    def getN(self):
        return self.__n

    def setSide(self, side):
        self.__side = side

    def getSide(self):
        return self.__side

    def setX(self, x):
        self.__x = x

    def getX(self, y):
        return self.__x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        area = self.__n * self.__side * self.__side / (4 * math.tan(math.pi / self.__n))
        return area


if __name__ == "__main__":
    regpol1 = RegularPoylgon()
    regpol2 = RegularPoylgon(6, 4)
    regpol3 = RegularPoylgon(10, 4, 5.6, 7.8)
    print("regpol1 的面积 =", regpol1.getArea())
    print("regpol1 的周长 =", regpol1.getPerimeter())
    print("regpol2 的面积 =", regpol2.getArea())
    print("regpol2 的周长 =", regpol2.getPerimeter())
    print("regpol3 的面积 =", regpol3.getArea())
    print("regpol3 的周长 =", regpol3.getPerimeter())

#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: Rectangle.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/01 16:59
@description:This file is fro ...  
"""


def func():
    pass


class Rectangle:
    def __init__(self, width=1.0, height=2.0):
        self.width = width
        self.height = height

    def setRectangle(self, width=1.0, height=2.0):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2.0 * (self.height + self.width)


if __name__ == "__main__":
    rect1 = Rectangle(4, 40)
    rect2 = Rectangle(3.5, 35.7)
    print("rect1 的面积 =", rect1.getArea())
    print("rect1 的周长 =", rect1.getPerimeter())
    print("rect2 的面积 =", rect1.getArea())
    print("rect2 的周长 =", rect1.getPerimeter())

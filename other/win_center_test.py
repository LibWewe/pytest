#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: win_center_test.py
@version: v1.0 
@author: WeWe 
@time: 2018/11/09 10:08
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro 将窗口设置为在屏幕中间显示
"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,
                             QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class CenterW(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()  # 将窗口居中放置的代码在自定义的center()方法中。
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 算出相对于显示器的绝对值。
        # 并且从这个绝对值中，我们获得了屏幕中心点。
        qr.moveCenter(cp)  # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
        # 矩形的大小并不会改变。
        self.move(qr.topLeft())  # 移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上。


def main():
    app = QApplication(sys.argv)
    ex = CenterW()
    sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()
    pass

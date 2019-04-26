#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: menuBar_test.py
@version: v1.0 
@author: WeWe 
@time: 2018/11/09 10:16
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,
                             QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('..\icon\Back.ico'), '&Exit', self)  # 创建菜单栏使用的菜单action
        exitAction.setShortcut('Ctrl+Q')  # 为菜单选项创建快捷键
        exitAction.setStatusTip('Exit application')  # 为菜单选项创建提示信息
        exitAction.triggered.connect(qApp.quit)  # 为菜单添加点击操作动作

        self.statusBar()  # 添加状态栏

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('&File')  # 为菜单栏添加菜单
        fileMenu.addAction(exitAction)  # 为菜单栏的菜单添加action

        self.setGeometry(300, 300, 300, 200)  # 设置窗口大小
        self.setWindowTitle('Menubar')  # 设置窗口标题名
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MenuBar()
    sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()
    pass

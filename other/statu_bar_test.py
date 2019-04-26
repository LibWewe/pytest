#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: statu_bar_test.py
@version: v1.0 
@author: WeWe 
@time: 2018/11/09 10:13
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


class StatusBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = StatusBar()
    sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()
    pass  












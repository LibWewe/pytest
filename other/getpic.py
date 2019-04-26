#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: 截屏.py
@version: v1.0 
@author: WeWe 
@time: 2018/03/09 16:10
@description:This file is fro ...  
"""

import time
import win32gui, win32ui, win32con, win32api
import tkinter
from tkinter.filedialog import askdirectory


def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w - 200, h - 200)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((-200, -200), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, "..\\images\\" + filename)


def capture_test():
    beg = time.time()
    for i in range(5):
        window_capture("haha.jpg")
    end = time.time()
    print(end - beg)


def capture_pic():
    timestr = time.strftime("%Y%m%d%H%M%S", time.localtime())
    window_capture(timestr + ".jpg")
    print(timestr)


def selectPath():
    path_ = askdirectory()
    path.set(path_)

path = ""
if __name__ == "__main__":

    win = tkinter.Tk()
    win.geometry("100x100+0+0")
    button = tkinter.Button(win, text="点击截图", command=capture_pic)
    button.place(x=0, y=10)
    #label = tkinter.Label(win, text="目标路径:").grid(row=0, column=0)
    #entry = tkinter.Entry(win, textvariable=path).grid(row=0, column=1)
    #button_setdir = tkinter.Button(win, text="路径选择", command=selectPath).grid(row=0, column=2)
    win.mainloop()

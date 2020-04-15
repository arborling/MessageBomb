#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import tkinter
from tkinter import *
from tkinter import ttk
import win32gui
import win32con
import win32clipboard


root = tkinter.Tk()
root.title("massage bomb v0.1")
Msg = StringVar()
Name = StringVar()


def send_message():
    msg = Msg.get()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,msg)
    win32clipboard.CloseClipboard()

    name_win = Name.get()
    handle = win32gui.FindWindow('TXGuiFoundation', name_win)
    # title = win32gui.GetWindowText(handle)
    # clsname = win32gui.GetClassName(handle)
    # childList = []
    # win32gui.EnumChildWindows(handle, lambda hwnd, param: param.append(hwnd), childList)
    # for i in childList:
    #     listwin.insert(i)

    n = 10
    while n != 0:
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        n = n-1


content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)

listwin = Listbox(frame)

sendbl = ttk.Label(content, text="Message:", font=('Arial', 10))
message = ttk.Entry(content, textvariable=Msg)

namebl = ttk.Label(content, text="name:", font=('Arial', 10))
name = ttk.Entry(content, textvariable=Name)

notice = ttk.Label(content, text="运行时注意：\n只保持一个QQ对话窗\n输入对象备注名和要发送的信息")

send = ttk.Button(content, text="Send", command=send_message)
stop = ttk.Button(content, text='Exit', command=root.quit)

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

listwin.grid(column=0, row=0, sticky=(N, S, E, W))

namebl.grid(column=3, row=0,  sticky=(N, W), padx=5)
name.grid(column=3, row=1,  sticky=(N, W), pady=5, padx=5)

sendbl.grid(column=4, row=0, columnspan=2, sticky=(N, W), padx=5)
message.grid(column=4, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

notice.grid(column=3, row=1)

send.grid(column=3, row=3)
stop.grid(column=4, row=3)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.mainloop()


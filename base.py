#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  #控件基础包，导入这个包后，这个包下的所有函数可以直接调用
import Tkinter
from Tkinter import Label, Button, END
import ttk
from Tix import Tk, Control, ComboBox  #升级的组合控件包
from tkMessageBox import showinfo, showwarning, showerror #各种类型的提示框
#除此之外还有很多界面编程的包

#顶层窗口
top = Tkinter.Tk()  #创建顶层窗口
top.geometry('650x550')  #初始化窗口大小
top.title("标题")
top.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件


#标签控件
label = Tkinter.Label(top, text='Hello World!',font='Helvetica -12 bold')   #创建标签
label.pack(fill=Y, expand=1)  #填充到界面

def btnClick():
    button.config(bg='yellow',text = cb.pick(2),fg = 'black')
    showwarning("你好呀",cb2.get())
#按钮控件
button = Tkinter.Button(top, text='QUIT',command=btnClick,activeforeground='white',activebackground='green', bg='red', fg='white')  #创建按钮，command为回调函数
button.pack(fill=Tkinter.X, expand=1) #fill=tkinter.X表示横向拉伸完全


#自定义函数，控制控件的缩放
def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())
    button.config(font= 'Helvetia  -%d bold' % scale.get())

#比例尺控件
scale = Scale(top, from_=10, to=40,orient=HORIZONTAL, command=resize)  #缩放比例尺
scale.set(12)  #初始值
scale.pack(fill=X, expand=1)  #填充到界面

#NumericUpDown控件
ct = Control(top, label='Number:',integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack(side = 'left')

#ComboBox控件
cb = ComboBox(top, label='Type:', editable=True)
for animal in ('dog', 'cat', 'hamster', 'python'):
    cb.insert(END, animal)
cb.pack(side = 'right')
#ComboBox控件
cb2_values = ['dog', 'cat', 'hamster', 'python'];
cb2 = ttk.Combobox(top, width=12,values = cb2_values)
cb2.pack(side = 'left')


Tkinter.mainloop()  #运行这个GUI应用
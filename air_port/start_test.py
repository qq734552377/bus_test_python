#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/8/16.

from Tkinter import *
from tkMessageBox import *
import ttk
from ScrolledText import *
import time
import os
import webbrowser
from multiprocessing import Process,Queue

def cmd(cmdStr):
    try:
        user_str = os.popen(cmdStr).read().strip()
        return user_str
    except Exception:
        return "执行命令行出错"

def cmdIsFailed(cmdStr):
    return os.system(cmdStr)

#获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time

#日志动态打印
def write_log_to_Text(logmsg):
    current_time = get_current_time()
    logmsg_in = str(current_time) +" ->" + str(logmsg) + "\n"
    log_txt.insert(END, logmsg_in)

def manu_increment():
    for i in range(100):
        progress1["value"] = i+1
        init_window.update()
        time.sleep(0.1)



class MyProcess(Process):
    def __init__(self,queue ):
        Process.__init__(self)
        self.queue = queue

    def run(self):
        time.sleep(3)
        result = cmd("./LightUp 1 hello*wold 2 ni*hao")
        self.queue.put(result)

def startTask():
    text_msg.set(u'正在打开红灯1，请稍后...')
    start_btn.config(state = 'disable')
    log_txt.delete('1.0', END)
    write_log_to_Text('请稍后...')
    progress1.start(15)
    global queue
    queue = Queue()
    p = MyProcess(queue)
    p.start()

    while(queue.empty()):
        init_window.update()
        time.sleep(0.01)

    write_log_to_Text(queue.get_nowait())
    progress1.stop()
    start_btn.config(state = 'active')
    # log_txt.tag_add('link', '2.0', END)
    # log_txt.tag_config('link', foreground='blue', underline=TRUE)
    pass

def show_arrow_cursor(event):
    log_txt.config(cursor='arrow')

def show_xterm_cursor(event):
    log_txt.config(cursor='xterm')

def link_click(event):
    webbrowser.open('http://www.baidu.com')

def center_window(root,w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def init_window_gui(root):
    global start_btn
    start_btn = Button(root,
           text=u'开始执行',
           bg='white',font=('Arial', 18 ,'bold'),
           command = startTask
           )
    start_btn.pack(pady=10)

    global text_msg
    text_msg = StringVar()
    text_msg.set(u'')
    # Label(root, textvariable=text_msg,
    #       bg='white',
    #       font=('Arial', 14),
    #       height = 4,
    #       wraplength = 420,
    #       justify = 'left'
    #       ).pack(fill=X,pady =5)

    global progress1
    progress1 = ttk.Progressbar(root, mode="indeterminate", orient=HORIZONTAL)
    progress1.pack(pady=5,padx=5,fill=X)
    # progress1["maximum"] = 100
    # progress1["value"] = 0


    global log_txt
    log_txt = ScrolledText(root,font=('Arial', 12),padx = 5,pady = 10)
    log_txt.pack(pady = 5,padx = 5,fill = BOTH,expand = TRUE)

    #<Enter>指的是当鼠标进入的时候调用show_hand_cursor函数
    log_txt.tag_bind('link', '<Enter>', show_arrow_cursor)
    log_txt.tag_bind('link', '<Leave>', show_xterm_cursor)
    log_txt.tag_bind('link', '<Button-1>', link_click)

    pass



def gui_start():
    global init_window
    init_window = Tk() #实例化出一个父窗口
    center_window(init_window,500,500)
    init_window.title("Air Port Test")
    # init_window.resizable(0,0)
    init_window_gui(init_window)

    init_window.mainloop()
    pass


if __name__ == "__main__":
    gui_start()
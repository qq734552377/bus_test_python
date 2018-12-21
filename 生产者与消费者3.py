#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/4.

import threading

alist = None
condition = threading.Condition()

def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        print "doSet前：" , alist
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        print 'doSet后：' , alist
        condition.release()

def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        print 'doPrint：' , alist
        condition.release()

def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            print "doCreate中：",alist
            condition.notifyAll()
        condition.release()

tset = threading.Thread(target=doSet,name='tset')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')
tset.start()
tprint.start()
tcreate.start()


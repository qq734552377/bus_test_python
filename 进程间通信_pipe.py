#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/4.

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    child_conn ,parent_conn= Pipe()   #返回成对出现的管道
    p = Process(target=f, args=(child_conn,))
    p.start()
    print parent_conn.recv()   # prints "[42, None, 'hello']"
    p.join()
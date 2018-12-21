#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/4.

from multiprocessing import Process, Queue
import time
def f(q):
    time.sleep(3)
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
      # prints "[42, None, 'hello']"
    # p.join()

    print "主线程感完了"
    print q.get()
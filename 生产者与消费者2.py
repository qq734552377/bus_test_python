#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/4.



import threading
import time

condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1;
                    print "Producer(%s):deliver one, now products:%s" %(self.name, products)
                    condition.notify()#不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print "Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products)
                    condition.wait();#自动释放锁定
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print "Consumer(%s):consume one, now products:%s" %(self.name, products)
                    condition.notify()
                    condition.release()
                else:
                    print "Consumer(%s):only 1, stop consume, products:%s" %(self.name, products)
                    condition.wait();
                time.sleep(2)

if __name__ == "__main__":
    for p in range(0, 4):
        p = Producer()
        p.start()

    for c in range(0, 2):
        c = Consumer()
        c.start()


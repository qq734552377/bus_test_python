#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/8/23.

import serial


def test():
    try :
        avr0 = serial.Serial("/dev/ttys2",115200,timeout=2)

        avr0.write("i am python")

        print "发送完成"


        while 1:
            result = avr0.read(20)
            print result
        avr0.close()
    except Exception:
        print "打开串口错误"
        return

if __name__ == "__main__":
    test()
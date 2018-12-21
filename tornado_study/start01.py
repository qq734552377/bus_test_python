#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/12.

import tornado.web
import tornado.ioloop
import tornado.httpserver # 新引入httpserver模块
import config

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast mi mi !")

class BootSelectHandle(tornado.web.RequestHandler):

    def get(self):
        self.render("a.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/b", BootSelectHandle)
    ], **config.settings)

    # ------------------------------
    # 我们修改这个部分
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    # ------------------------------
    tornado.ioloop.IOLoop.current().start()
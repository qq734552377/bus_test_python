#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/12.
import os

# Redis配置
redis_options = {
    'redis_host':'127.0.0.1',
    'redis_port':6379,
    'redis_pass':'',
}

# Tornado app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies':False,
    'login_url':'/login',
    'debug':True,
}

# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/7.

import requests

url_file = 'http://www.ucast.sg/components/jquery/jquery-3.1.1.min.js'


def smallFileDown(url,file_path):
    r = requests.get(url)
    with open(file_path,'wb') as f: #with语句访问文件，不论文件是否操作成功都会最终执行close()
        f.write(r.content)

def bigFileDown(url,file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/7.

from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'

@app.route('/bootstrap_select')
def bootstrap_select():
    return render_template('a.html')



















if __name__ == "__main__":
    app.run()
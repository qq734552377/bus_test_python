#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by pj on 2018/6/7.

from lxml import etree

wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """
html = etree.HTML(wb_data)
def baseMsg():
    print html
    result = etree.tostring(html)
    print result.decode("utf-8")

def getText_1():
    #通过绝对路径找到a标签
    html_data = html.xpath('/html/body/div/ul/li/a')
    print(html_data)
    for i in html_data:
        print(i.text)

def getText_2():
    #通过绝对路径照a标签并去里面的内容
    html_data = html.xpath('/html/body/div/ul/li/a/text()')
    print(html_data)
    for i in html_data:
        print(i)

def getText_3():
    #查到绝对路径下a标签属性等于link2.html的内容
    html_data = html.xpath('/html/body/div/ul/li/a[@href="link2.html"]/text()')
    print(html_data)
    for i in html_data:
        print(i)

def getText_4():
    #查找相对路径
    html_data = html.xpath('//li/a/text()')
    print(html_data)
    for i in html_data:
        print(i)

def getText_5():
    #相对路径下跟绝对路径下查特定属性的方法类似
    html_data = html.xpath('//li/a[@href="link2.html"]')
    print(html_data)
    for i in html_data:
        print(i.text)

def getText_6():
    #查找最后一个li标签里的a标签
    html_data = html.xpath('//li[last()]/a/text()')
    print(html_data)
    for i in html_data:
        print(i)

def getText_7():
    #查找倒数第二个li标签里的a标签
    html_data = html.xpath('//li[last() - 1]/a/text()')
    print(html_data)
    for i in html_data:
        print(i)

def openHtmlFile(path):
    #使用parse打开html的文件
    with open(path) as f:
        html = etree.HTML(f.read())
        html_data = html.xpath('/html/body')#打印是一个列表，需要遍历
        print(html_data)
        for i in html_data:
            print(i.text)

def getAttr_1():
    #打印指定路径下a标签的属性
    html_data = html.xpath('/html/body/div/ul/li/a/@href')
    for i in html_data:
        print(i)

def getAttr_2():
    #l相对路径下li标签下的a标签下的href属性的值
    html_data = html.xpath('//li/a/@href')
    print(html_data)
    for i in html_data:
        print(i)




if __name__ == "__main__":
    getAttr_2()


    pass
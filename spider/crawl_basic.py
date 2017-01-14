#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 网络爬虫主要分为：url管理模块，网页下载模块，网页解析模块
"""
import urllib2
from bs4 import BeautifulSoup


# 直接通过url 进行访问
# 下载网页资源----可能网站并不存在会抛出异常
def get_web_content(test_url):
    try:
        response = urllib2.urlopen(test_url)
    except Exception as e:
        return None
    # 创建beautifulSoup解析器
    try:
        bp = BeautifulSoup(response.read(), "html.parser", from_encoding="utf-8")
        tit=bp.title
        # 通过css 来获取节点
        answer = bp.find_all("div", {"class":"zm-editable-content"})

        answer_lst=[ans.get_text() for ans in answer]
        # 将爬去到节点保存到文本中

        with open("./zhihu.txt", "w") as f:
            for an in answer_lst:
                f.write('%s\n' % an.encode("utf-8"))
    except Exception as e:
        print e
        return None
    else:
        return tit


test_url = "https://www.zhihu.com/question/20691338"
title = get_web_content(test_url)
if title is not None:
    print title.get_text()
else:
    print "网页不存在，请重新输入网页地址！"

# 将请求访问封装为浏览器请求方式
request = urllib2.Request(test_url)
request.add_header("user-agent", "Mozilla/5.0")
responses = urllib2.urlopen(request)

# 下载网页首页

# 对页面进行解析
# 常用的方法有正则表达式，html.parser,beautifulSoup----结构化的网页解析器，lxml等

# 创建beautifulSoup 对象
# zhihu_doc = response.read()

# bp = BeautifulSoup(zhihu_doc, "html.parser", from_encoding="utf-8")

# 提取所有的知乎回答
# 根据属性提取获节点
# answer = bp.find("span", class_="js-voteCount")
# 遍历获取到的所有值
# print  answer.name, answer.get_text(),

# for anw in answer:
#     print anw.name,anw["class_"]

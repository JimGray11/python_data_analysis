#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
 beautifulSoup 解析网页的高阶方法
"""
from bs4 import BeautifulSoup
import urllib2
import  re
test_url = "https://www.amazon.cn/gp/bestsellers/books/" \
           "ref=br_bsl_smr/456-4063020-4086765?pf_rd_m=A1AJ19PSB66TGU&" \
           "pf_rd_s=desktop-bestsellers-2&pf_rd_r=34EJ9KWD8JZF00TKW2V3&pf_rd_r" \
           "=34EJ9KWD8JZF00TKW2V3&pf_rd_t=36701&pf_rd_p=777b26ab-395a-4110-95ea-35430219c976&pf_rd_p" \
           "=777b26ab-395a-4110-95ea-35430219c976&pf_rd_i=desktop"

test_url2 = "http://www.pythonscraping.com/pages/page3.html"


def beauatiful_soap_advance(test_url):
    request = urllib2.Request(test_url)
    request.add_header("user-agent", "Mozilla/5.0")
    response = urllib2.urlopen(request)
    # 使用beatifulSoup 解析网页
    bp = BeautifulSoup(response.read(), "html.parser", from_encoding='utf-8')

    # 根据孩子节点进行遍历-----childern是属性不是方法
    content_descendants = bp.find("table", {"id": "giftList"}).descendants
    print  type(content_descendants)
    # print "*********************descendants 使用子孙节点*****************"
    # 注意使用descendants返回的generator 使用children 返回的是listIterator
    get_iterator_node(content_descendants)
    print "===============使用children来查找节点=================="
    content_childern = bp.find("table", {"id": "giftList"}).children
    print type(content_childern)
    get_iterator_node(content_childern)
    print "==================使用同辈节点next_siblings访问节点=========="
    content_next_siblings = bp.find("table", {"id": "giftList"}).tr.next_siblings
    get_iterator_node(content_next_siblings)
    print "===========调用parent =============="
    content_parent_previous_siblings = bp.find("img", src="../img/gifts/img6.jpg").parent.previous_siblings
    get_iterator_node(
        content_parent_previous_siblings
    )


def get_iterator_node(conent_lst):
    for i, content in enumerate(conent_lst
                                ):
        if i == 1 or content.name is None:
            continue
        else:
            print "============================================="
            print content.name
            print content
            print content.get_text()


if __name__ == "__main__":
    # beauatiful_soap_advance(test_url2)
    a=re.compile("^(/view/)((?!:).)*$")
    # 表示可以使用除了：之外的任意字符
    rs=a.match("/view/........")
    print rs.group()

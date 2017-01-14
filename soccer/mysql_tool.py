# -*- coding: utf-8 -*-
"""
  主要定义操作数据库的方法
"""
import MySQLdb as db
import logging


def get_mysql_connect():
    # 获取MySql数据库连接
    con = db.connect(host='localhost', port=3306, user='root', passwd='root', db='soccer',charset='utf8')
    # 获取对应操作游标
    cursor = con.cursor()
    return con, cursor


def commit_close(con):
    # 提交数据数据
    if con:
        con.close()
    else:
        print("当前连接不存在")
    '''
    TODO 此处将来使用日志来处理
    '''

# -*- coding: utf-8 -*-
"""
主要用于数据的ETL操作-----从数据库中取出数据，并对数据进行转换，返回
"""

import datetime
import time
import numpy as np


def get_player_basic_info(cursor, num):
    sql = "select player_api_id,player_name,birthday,height,weight from player limit %d" % num
    cursor.execute(sql)
    players = cursor.fetchall()
    return players


def get_age_by_birthday(birthday):
    # 将出生年月日((1992-02-29 00:00:00))转换为日期
    dt = datetime.datetime.strptime(birthday.split(" ")[0], '%Y-%m-%d')
    # 获取当前时间
    td = datetime.datetime.now()

    return td.year - dt.year - ((dt.month, dt.today) < (td.month, td.today))


def get_player_avg(cursor, player_api_id):
    cursor.execute("select overall_rating from player_attributes where player_api_id = %s" % player_api_id)
    all_rating = cursor.fetchall()
    nd = np.array(all_rating, dtype=np.float)[:, 0]
    # 对矩阵求平均值
    return np.nanmean(nd, dtype=np.float)


def get_country_team(cursor, player_api_id):
    # 获取球员所在的球队，国家，以及曾经所在的球队个数
    rate = get_player_avg(cursor, player_api_id)
    # rate>0 表示该球员参加过比赛
    if rate > 0:
        nums = [x for x in reversed(range(1, 12))]
        sql = "select home_team_api_id, country_id from matchs where  home_player_%d = '%d'"
        for num in nums:
            cursor.execute(sql % (num, player_api_id))
            country_team_id_lst = cursor.fetchall()
            if len(country_team_id_lst) > 0:
                number_teams = len(np.unique(np.array(country_team_id_lst)[:, 0]))
                # country_team_id_lst[-1][0]表示选择最后一行的第一列
                last_team_id = country_team_id_lst[-1][0]
                last_country_id = country_team_id_lst[-1][1]
                cursor.execute("select team_long_name FROM Team WHERE team_api_id = '%d'" % last_team_id)

                last_team_name = cursor.fetchall()[0][0]
                cursor.execute("sELECT name FROM Country WHERE id = '%d'" % last_country_id)

                last_country_name = cursor.fetchall()[0][0]

                return last_country_name, last_team_name, number_teams

    return None, None, 0

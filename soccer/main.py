#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql_tool as db
import get_data_from_db as gt
import pandas as pd
import mpl_toolkits.basemap as bm
import matplotlib.pyplot as plt
import numpy as np


def run_task_data(cursor):
    """
    多表查询获取球员的基本数据，并返回，同时将数据转换为csv文件格式保存
    基本数据信息包括：
    姓名，生日，体重，身高
    -----年龄------根据生日得到计算年龄,平均评分-------在Player_Attributes中根据player_api_id来获取
    -----所在的球队，国家，曾经所在的球队个数------country,team
    :param cursor:
    :return: 返回球员的数据
    """
    # 设置需要分析球员的个数
    max_player_to_analysis = 100
    players = gt.get_player_basic_info(cursor, max_player_to_analysis)

    # player_api_id，player_name，birthday，height，weight
    # 查询出来的list可以列名或许相应列的值
    player_api_id_lst, player_name_lst, birthday_lst, height_lst, weight_lst = zip(*players)
    # 根据出生日期计算年龄
    player_age_lst = [age for age in map(gt.get_age_by_birthday, birthday_lst)]

    # 计算平均评分列表----球员的评分在球员属性中，需要根据player_api_id来获取其所有的评分才能计算出平均分
    player_avg_lst = [gt.get_player_avg(cursor, player_api_id) for player_api_id in player_api_id_lst]

    player_country_team_lst = [gt.get_country_team(cursor, player_api_id) for player_api_id in player_api_id_lst]

    # 解析出国家，球队，曾经所在的球队个数
    coutry_ls, team_lst, team_nums = zip(*player_country_team_lst)

    # 将所有的属性数据保存为scv的格式

    player_name = pd.Series(player_name_lst, name="name")
    player_age = pd.Series(player_age_lst, name='age')
    weight = pd.Series(weight_lst, name="weight")
    height = pd.Series(height_lst, name="height")
    player_avg = pd.Series(player_avg_lst, name='avg')
    coutry = pd.Series(coutry_ls, name='country')
    team = pd.Series(team_lst, name='team')
    num = pd.Series(team_nums, name='total')

    df = pd.concat([player_name, player_age, weight, height, coutry, team, player_avg, num], axis=1)
    with open('./player.csv', 'w') as f:
        df.to_csv(f, index=None, encoding='utf-8')

    return df


def run_task_view(df):
    """
     主要实现的是可视化展示------可视化国家的平均分
    :param df:
    :return:
    """
    # 计算国家同一个国家之间的平均分
    country_rating = df.groupby("country")["avg"].mean()  # 此处会形成Series-----定长的有序字典
    # 对coutry_rating 重新设置索引---可以将Serires 变成DataFrame
    country_rating = country_rating.reset_index()
    # 获取到得分最少的国家
    min_avg = country_rating["avg"].min()

    # 按国家计算整体评分
    avg_cof = map(lambda x: x - min_avg + 5, country_rating["avg"])
    country_rating["avg"] = avg_cof

    # 使用dataFrame 构建字典列表
    counrys = {item[0]: item[1] for item in country_rating.values}

    # 初始化地图信息
    countries = {}
    # [横坐标, 纵坐标, 点大小]
    countries["England"] = [-0.12, 51.5, 20.0]
    countries["Belgium"] = [4.34, 50.85, 20.0]
    countries["France"] = [2.34, 48.86, 20.0]
    countries["Germany"] = [13.4, 52.52, 20.0]
    countries["Italy"] = [12.49, 41.89, 20.0]
    countries["Netherlands"] = [4.89, 52.37, 20.0]
    countries["Poland"] = [21.01, 52.23, 20.0]
    countries["Portugal"] = [-9.14, 38.73, 20.0]
    countries["Scotland"] = [-4.25, 55.86, 20.0]
    countries["Spain"] = [-3.70, 40.41, 20.0]
    countries["Switzerland"] = [6.14, 46.2, 20.0]

    # 更新地图中的点大小
    for country_name in counrys.keys():
        countries[country_name][2] = 3 * counrys[country_name]
    plt.figure(figsize=(12, 12))

    # 开始画地图
    m = bm.Basemap(projection='cyl',  # 地图投影方式
                   llcrnrlat=35, urcrnrlat=58, llcrnrlon=-10, urcrnrlon=22,  # 经纬度范围
                   resolution='f')
    # 绘制国家
    for i in countries.keys():
        m.plot(countries[i][0], countries[i][1], 'bo', markersize=countries[i][2], color='r')

    # 添加国家名称
    for label, xpt, ypt in zip(list(countries.keys()), np.array(list(countries.values()))[:, 0], \
                               np.array(list(countries.values()))[:, 1]):
        plt.text(xpt - 0.85, ypt, label, fontsize=20, color="black")
    plt.show()

    return None


if __name__ == "__main__":
    con, cursor = db.get_mysql_connect()
    # 从数据库中获取相关的数据
    result = run_task_data(cursor)
    # 根据数据result使用basemap画图
    run_task_view(result)

    try:
        if con:
            con.close()
    except:
        print "数据库连接不存在"

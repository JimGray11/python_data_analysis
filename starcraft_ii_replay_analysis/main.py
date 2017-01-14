#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 分析星球争霸II中各个战队的属性情况，得到相应结论
 提取字段属性：
 LeagueIndex-----战队编号
 age ------ 年龄
 HoursPerWeek------每周玩的时长
 WorkersMade -------单位时间建造数
 APM------每分钟操作次数
"""
import pandas as pd
from pandas_tools import inspect_data, process_missing_data, visualize_league_attributes, \
    visualize_league_attribute_stats


# 打开数据文件
def run_main(dist_path):
    # 打开数据文件
    df = pd.read_csv(dist_path, usecols=['LeagueIndex', 'Age', 'HoursPerWeek', 'WorkersMade', 'APM'])
    # 查看数据
    inspect_data(df)
    # 处理缺失数据
    process_missing_data(df)
    # 可视化战队属性
    visualize_league_attributes(df)
    # 可视化战队属性统计
    visualize_league_attribute_stats(df, "HoursPerWeek", "./dataset/HoursPerWeek.csv", "./dataset/HoursPerWeek.jpg")
    visualize_league_attribute_stats(df, "APM", "./dataset/APM.csv", "./dataset/APM.jpg")

if __name__ == "__main__":
    dist_path = "./dataset/starcraft.csv"
    run_main(dist_path)

# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

"""
主要为对数据分析中的一些常用方法的封装
"""


def inspect_data(df):
    # 查看数据的格式
    print '数据有%d行，有%d列' % (df.shape[0], df.shape[1])
    # 查看列的详细信息
    print df.info()
    print df.head()


def process_missing_data(df):
    # 处理缺失的数据
    if df.isnull().values.any():
        # 在调用方法isnull()之后，形成一个bool矩阵，使用values 获取属性值
        # 存在缺失数据-----将缺失数据删除，或者使用默认值来填充缺失数据
        df = df.fillna(0.)
    return df


def visualize_league_attributes(df, save_fig=True):
    """
    可视化战队属性
    :param df:
    :return:
    """
    # 创建figure
    fig = plt.figure(figsize=(15.0, 10.0))
    # 将figure 切分为几个小的区域
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    # 解决matplotlib 中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像负号"-" 显示为方块问题
    # 设置标题
    fig.suptitle(u"星空争霸II战队情况分析")
    # 在各个子画板画图
    ax1.scatter(df["LeagueIndex"], df["HoursPerWeek"])
    ax1.set_xlabel(u"战队")
    ax1.set_ylabel(u"每周的游戏时间")

    ax2.scatter(df["LeagueIndex"], df["Age"])
    ax2.set_xlabel(u"战队")
    ax2.set_ylabel(u"玩家你年龄")

    ax3.scatter(df["LeagueIndex"], df["APM"])
    ax3.set_xlabel(u"战队")
    ax3.set_ylabel(u"每分钟手速")

    ax4.scatter(df["LeagueIndex"], df["WorkersMade"])
    ax4.set_xlabel(u"战队")
    ax4.set_ylabel(u"单位时间的建造数")

    if save_fig:
        plt.savefig("./dataset/attributes.jpg")

    plt.show()


def visualize_league_attribute_stats(df, attribute, save_data_path='', sava_fig_path=''):
    starcraft_idx_lst = range(1, 9)
    # 选出不同战队的数据
    stats_min = []  # 找出各个战队中的最小值
    stats_max = []  # 找出各个战队中的最大值
    stats_mean = []  # 计算出各个战队中的平均值
    for id in starcraft_idx_lst:
        # pandas 中的过滤,使用标签索引
        filter_data = df.loc[df["LeagueIndex"] == id, attribute]
        stats_min.append(filter_data.min())
        stats_max.append(filter_data.max())
        stats_mean.append(filter_data.mean())
    # 将list 转换为转换为Series
    indx_ser = pd.Series(starcraft_idx_lst, name="LeagueIndex")
    stats_min_ser = pd.Series(stats_min, name='min')
    stats_max_ser = pd.Series(stats_max, name='max')
    stats_mean_ser = pd.Series(stats_mean, name="mean")

    # 将系列拼接成一个DataFrame 存入csv文件
    result = pd.concat([indx_ser, stats_min_ser, stats_max_ser, stats_mean_ser], axis=1)
    # 判断结果文件是否需要保存
    if save_data_path != '':
        result.to_csv(save_data_path, index=None)
    # 将统计值可视化

    # 解决matplotlib 中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像负号"-" 显示为方块问题

    fig = plt.Figure(figsize=(15.0, 10.0))
    fig.add_subplot(1, 1, 1)
    plt.plot(result["LeagueIndex"], result['min'], color='b')
    plt.plot(result["LeagueIndex"], result['max'], color='r')
    plt.plot(result["LeagueIndex"], result['mean'], color='g')

    plt.xlabel(u"战队")
    plt.ylabel(attribute)
    plt.title(attribute + u"vs 星球争霸联盟")

    # 需要标注每条线表示的意思
    min_line = mpatches.Patch(color='blue', linewidth=0.2, label="min")
    max_line = mpatches.Patch(color='red', linewidth=0.2, label='max')
    mean_line = mpatches.Patch(color='green', linewidth=0.2, label="mean")

    plt.legend(handles=[min_line, max_line, mean_line], loc=2)
    if sava_fig_path != '':
        plt.savefig(sava_fig_path)
    plt.show()

    return None

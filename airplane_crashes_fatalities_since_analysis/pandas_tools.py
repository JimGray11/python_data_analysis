# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.io import output_file, show
from bokeh.charts import Bar, TimeSeries
from bokeh.layouts import column
from math import pi


def inspect_data(df_data):
    print "**************************************************"
    print "数据集中有%d 行,有%d列" % (df_data.shape[0], df_data
                              .shape[1])
    print "数据集中的列信息如下："
    print df_data.info()
    print "数据集中的示例数据如下："
    print df_data.head(2)
    print "***************************************************"
    return None


def process_missing_data(df_data):
    """
    处理缺失的数据，fillna() 或者是dropna()
    :param df_data:
    :return:
    """
    if df_data.isnull().values.any():
        print "---------存在缺失的数据----------"
        df_data = df_data.fillna(0.)
    return df_data


def convert_data_time(df_data):
    """
    实现Date列中时间格式的统一，同时从时间中提取单独年份作为单独的一列添加到数据集上
    :param df_data:
    :return:
    """
    # 实现DataFrame 中date列的格式转换
    df_data["Date"] = pd.to_datetime(df_data["Date"])
    # 如果在DataFrame中列不存在就会自动添加一列
    df_data["year"] = df_data["Date"].map(lambda x: x.year)
    return df_data


def plot_crashes_vs_year(df_data, method, save_fig=True):
    """
     实现对每年空难数之间的统计
    :param df_data: 数据集
    :param method: 可视化方法
    :param save_fig: 默认是保存可视化的结果的
    :return:  None
    """
    # year = df_data.groupby("year")["year"].count()
    # 使用seaborn 来画图
    if method == 'sns':
        plt.figure(figsize=(15.0, 10.0))
        sns.countplot(x=df_data["year"], data=df_data)
        # 解决画图中的中文乱码问题
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        # 设置标签
        plt.title(u"空难数vs年份")
        plt.xlabel(u"年份")
        plt.ylabel(u"空难数")
        # 设置显示刻度
        plt.xticks(rotation=90)

        if save_fig:
            plt.savefig('./output/crashes_year.png')

        plt.show()
    elif method == 'bokeh':
        # 使用bokeh的方式画图
        p = Bar(df_data, 'year', title='空难次数 vs 年份',
                plot_width=1000, legend=False, xlabel='年份', ylabel='空难次数')
        p.xaxis.major_label_orientation = pi / 2
        output_file('./output/crashes_year.html')
        show(p)

    else:
        print '不支持的绘图方式！'
    return None


def plot_aboard_fatalities_year(df_data, method, save_fig=True):
    """
    分析在每年的空难中遇难飞机上的乘机人数和遇难人数
    :param df_data:
    :param method:
    :param save_fig:
    :return:
    """
    groupby_year_sum_data = df_data.groupby('year', as_index=False).sum()
    if method == 'sns':
        plt.figure(figsize=(18.0, 15.))
        sns.barplot(x='year', y='Aboard', data=groupby_year_sum_data, color='red')
        sns.barplot(x='year', y='Fatalities', data=groupby_year_sum_data, color='green')
        # 解决matplotlib显示中文问题
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        # 设置显示刻度
        plt.xticks(rotation=90)
        plt.xlabel(u'年份')
        plt.ylabel(u'人数')
        plt.title(u'乘客数量vs遇难人数')
        if save_fig:
            plt.savefig('./output/aboard_fatalities_sum.jpg')
        plt.show()
    elif method == 'bokeh':
        # Boken 绘图
        tsline = TimeSeries(data=groupby_year_sum_data,
                            x='year', y=['Aboard', 'Fatalities'],
                            color=['Aboard', 'Fatalities'], dash=['Aboard', 'Fatalities'],
                            title='乘客数vs遇难数vs年份', xlabel='年份', ylabel='乘客数vs遇难数',
                            legend=True)
        tspoint = TimeSeries(data=groupby_year_sum_data,
                             x='year', y=['Aboard', 'Fatalities'],
                             color=['Aboard', 'Fatalities'], dash=['Aboard', 'Fatalities'],
                             builder_type='point',
                             title='乘客数vs遇难数vs年份', xlabel='年份', ylabel='乘客数vs遇难数',
                             legend=True)
        output_file('./output/aboard_fatalities_year.html')
        show(column(tsline, tspoint))
    else:
        print '不支持的绘图方式！'
    return None


def get_top_n(df_data, col_name, top_n, save_file_path="", save_fig_path=""):
    """
    分析空难数最多的前n种机型/operator
    :param df_data:
    :param col_name:
    :param save_file_path: 保存数据文件的路径
    :return:
    """
    stats_data = df_data.groupby(by=col_name, as_index=False)["Date"].count()
    stats_data = stats_data.rename(columns={"Date": "count"})
    sort_stats_data = stats_data.sort_values("count", ascending=False).iloc[:top_n, :]
    # 将数据单独保存在csv 文件中
    if save_file_path != "":
        sort_stats_data.to_csv(save_file_path)
    # 数据可视化化
    plt.figure(figsize=(15.0, 12.0))
    sns.barplot(x='count', y=col_name, data=sort_stats_data)

    # 设置标题
    plt.title(u"count vs %s" % col_name)
    plt.xlabel(u"%s" % col_name)
    plt.ylabel(u"count")
    if save_fig_path != "":
        plt.savefig(save_fig_path)
    plt.show()
    return None

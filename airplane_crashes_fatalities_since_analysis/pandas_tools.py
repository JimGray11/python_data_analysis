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

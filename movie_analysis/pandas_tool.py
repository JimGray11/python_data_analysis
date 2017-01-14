# -*- coding:utf-8 -*-
import pandas as pd
import os

"""
  主要实现如下功能：
  1.查看数据
  2.处理缺失数据
"""


def inspect_data(df_data):
    print "数据总共有%d行%d列" % (df_data.shape[0], df_data.shape[1])
    print "****************DataFrame的基本列属性信息如下**************"
    print df_data.info
    print "******************示例数据如下****************************"
    print df_data.head(2)


def process_missing_data(df_data):
    if df_data.isnull().values.any():
        # 将缺失的数据的行直接删除
        df_data = df_data.dropna()
        return df_data.reset_index()


def attribute_statistics_gross(df_data, attributes_analysis, save_path=""):
    """
     主要是根据不同属性来分析和票房收入之间的关系
    :param df_data:
    :param attributes_analysis:
    :param save_path:
    :return:
    """
    df_data = df_data.groupby(attributes_analysis, as_index=False)["gross"].sum()
    # 将统计好的数据进行排序，保存到文件中
    sorted_gross = df_data.sort_values(by='gross', ascending=False)
    sorted_gross.to_csv(save_path, index=None)
    return None


def get_genres_data(df_data):
    # 如何将现有的数据变成新的DataFrame
    file_path = "./output/df_genres.csv"

    if os.path.exists(file_path):
        df_genres = pd.read_csv(file_path)
    else:
        df_genres = pd.DataFrame(columns=['genre', 'budget', 'gross', 'year'])
        for id, row_data in df_data.iterrows():
            if (id + 1) % 100 == 0:
                print "已经处理了%s 条数据" % id
            df_data = convert_row_data(row_data)
            # 将为一行数据拼接成的DataFrame
            df_genres = df_genres.append(df_data, ignore_index=True)
        df_genres.to_csv(file_path, index=None)

    return df_genres


def convert_row_data(row_data):
    """
    将每一行的数据重构成DataFrame
    :param row_data:
    :return:
    """
    genres = row_data["genres"].split("|")

    # 需要将数据拷贝成几份
    rows = len(genres)
    # 先将数据拼接为dict{}的形式
    row_obj = {}

    row_obj["genre"] = genres
    row_obj["budget"] = [row_data["budget"]] * rows
    row_obj["gross"] = [row_data["gross"]] * rows
    row_obj["year"] = [row_data["title_year"]] * rows
    return pd.DataFrame(row_obj)

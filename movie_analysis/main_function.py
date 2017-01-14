# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas_tool import inspect_data, process_missing_data, attribute_statistics_gross, get_genres_data

"""
 一、查看数据
 二、处理缺失数据
 三、主要的分析指标如下：
 1.查看票房收入统计
   1.1 导演（director_name）vs票房总收入
   1.2 主演（actor_1_name）vs票房总收入
   1.3 导演+主演vs票房收入
 2.查看各imdb评分统计
   2.1查看各imdb 评分的电影个数-----比如电影7.9 的电影有10部
   2.2 查看top20 导演的平均imdb评分
   2.3 查看电影产量趋势
 3.电影类型分析
   3.1电影类型个数统计
   3.2电影类型票房统计
"""


def run_main():
    file_path = "./dataset/movie_metadata.csv"
    df_data = pd.read_csv(file_path)
    # 一、查看数据
    inspect_data(df_data)
    # 二、处理缺失数据
    df_data = process_missing_data(df_data)
    # １.查看票房收入统计
    # 1.1 查看导演和票房收入统计之间的关系
    attribute_statistics_gross(df_data, "director_name", "./output/director_gross.csv")
    # 1.2 分析1号主演和票房之间的关系
    attribute_statistics_gross(df_data, 'actor_1_name', "./output/actor_gross.csv")
    # 1.3 导演+主演和票房之间的关系
    attribute_statistics_gross(df_data, ['director_name', 'actor_1_name'], "./output/director_actor_gross.csv")
    # 2.查看imdb评分统计
    # 2.1 查看各imdb 评分的电影个数
    imdb_score_movie_count=df_data.groupby(["imdb_score"])["movie_title"].count()
    plt.figure()
    # 画图
    imdb_score_movie_count.plot()
    plt.savefig("./output/score_movie_count.jpg")
    plt.show()
    # 查看top20 导演的平均imdb评分
    diractor_avg_score=df_data.groupby("director_name")["imdb_score"].mean()
    # 对导演的平均分进行排序
    sort_director_avg_score=diractor_avg_score.sort_values(ascending=False)[:20]
    plt.figure(figsize=(20,10))
    sort_director_avg_score.plot(kind="bar")
    plt.savefig("./output/top20.jpg")
    plt.show()
    # 2.3 查看电影产量趋势
    movie_product_trend=df_data.groupby("title_year")["title_year"].count() # groupby 之后的数据为Series
    plt.figure()
    movie_product_trend.plot()
    plt.savefig("./output/trend.jpg")
    plt.show()
    # 3.电影类型分析
    # 3.1 电影类型个数统计
    df_genres = get_genres_data(df_data)  # 将原始数据进行

    movie_type_total = df_genres.groupby("genre").size()
    plt.figure(figsize=(18.0, 10.0))
    movie_type_total.plot(kind='bar')
    plt.savefig("./output/movie_type.jpg")
    plt.show()
    # 3.2 电影类型票房统计
    movie_type_gross_type = df_genres.groupby("genre")["gross"].sum()
    plt.figure(figsize=(18.0, 10.0))
    movie_type_gross_type.plot(kind='bar')
    plt.savefig("./output/movie_type_gross.jpg")
    plt.show()


if __name__ == '__main__':
    run_main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 读取不同类型
import pandas as pd
import json
import mpl_toolkits.basemap as bm

"""
txt_filename = "C:\\Users\\JimG\\Desktop\\数据科学电子书\数据分析\\lecture03_codes\\files\\presidential_polls.csv"

# 可以使用numpy 中loadtxt 来打开csv 格式的文件
df = pd.read_csv(txt_filename, usecols=['cycle', 'type', 'startdate'])
print(type(df))
print(df.head())

# 从DataFrame 根据列名获取series

ser = df['cycle']
print(type(ser))
print(ser.head())

# 将读取出来的数据写入csv 格式的文件中
txt_filename_out = "C:\\Users\\JimG\\Desktop\\数据科学电子书\数据分析\\lecture03_codes\\files\\out_put.csv"

df.to_csv(txt_filename_out, index=None)
"""
"""
# 读取json类型的字符串
file_dir = "C:\\Users\\JimG\\Desktop\\数据科学电子书\\数据分析\\lecture03_codes\\files\\global_temperature.json"
with open(file_dir, "r") as fp:
    data = json.load(fp)
# 将json 格式的数据转换为csv 取出data 中对应的所有key和value
file_out_dir = "C:\\Users\\JimG\\Desktop\\数据科学电子书\\数据分析\\lecture03_codes\\files\\temperature.csv"
# 如何设置csv 文件的第一行--------------在csv 中，对应一个列是一个series
year_str_lst = data["data"].keys()
values_str_lst = data["data"].values()
year_int_lst = [int(year) for year in year_str_lst]
year_float_lst = [float(value) for value in values_str_lst]

year = pd.Series(year_int_lst, name="year")
value = pd.Series(year_float_lst, name="value")
# 将两个Series拼接成dataFrame

df = pd.concat([year, value], axis=1)

df.to_csv(file_out_dir, index=None)

"""
# 将json  格式的数据写入文件

book_dict = [{'书名': '无声告白', '作者': '伍绮诗'}, {'书名': '我不是潘金莲', '作者': '刘震云'}, {'书名': '沉默的大多数 (王小波集)', '作者': '王小波'}]

filename = "C:\\Users\\JimG\\Desktop\\数据科学电子书\\数据分析\\lecture03_codes\\files\\json_out_data.json"
with open(filename, 'w') as f_obj:
    # 在输入数据中带有中文时，需要将ensure_ascii 设置为False
    f_obj.write(json.dumps(book_dict, ensure_ascii=False))

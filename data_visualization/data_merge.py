# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

"""
数据清洗，转换合并、重构和转换
"""
# 1 数据的合并使用merge操作
# 使用dict创建两个DataFrame
d1 = pd.DataFrame({"key1": ['b', 'b', 'a', 'c', 'd', 'd'],
                   'data1': np.random.randint(0, 10, 6)})
d2 = pd.DataFrame({"key2": ['b', 'a', 'd', 'h'],
                   'data2': np.random.randint(0, 10, 4)})
# 在merge时d1和d2有着相同的合并列名key,默认情况下将重叠列名作为外键进行合并,如果明确指出之时需要使用on
# print pd.merge(d1,d2)
# 如果是在d1和d2没有重叠列名时
# １、在连接键相同的情况下使用on, 如果连接键不相同需要使用left_on 和right_on来指名各自的外键
# print pd.merge(d1, d2, left_on="key1", right_on="key2")
# 2、如果不使用left_on 和right_on 时,可以使用修改列名 注意在rename 方法中columns={"列名":"新列名"}
d1 = d1.rename(columns={"key1": "key"})
d2 = d2.rename(columns={"key2": "key"})
# print pd.merge(d1,d2)
# 如果需要改变默认的inner连接方式，需要使用how='outer'------outer 表示外连接 left-----表示左外连接 right----表示右外连接
print pd.merge(d1, d2, how="outer")

d3 = pd.DataFrame({"key": ['b', 'b', 'a', 'c', 'd', 'd'],
                   'data': np.random.randint(0, 10, 6)})
d4 = pd.DataFrame({"key": ['b', 'a', 'd', 'h'],
                   'data': np.random.randint(0, 10, 4)})
# 解决重复列名问题
print pd.merge(d3, d4, on='key', how='left', suffixes=('_d3', '_d4'))
# 根据索引进行连接

d5 = pd.DataFrame({'data': np.random.randint(0, 10, 4)}, index=['b', 'a', 'd', 'h'])
print pd.merge(d3,d5,left_on='key',right_index=True,how='outer')

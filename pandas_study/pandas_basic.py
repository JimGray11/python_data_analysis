#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import datetime

"""
pandas的基础运用-----主要是Series 和 DataFrame
"""
# 使用list创建Series---默认的index 是从0的序列开始
dat1 = pd.Series(range(1, 10))
# print  dat1

# 使用dict创建Series----index 为key的值
dat2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# print  dat2

# 对Series的索引-----使用位置索引，标签索引，混合索引

# print dat1[0], dat2['a']
# print dat1[1:10:2]
# print dat2['a':'c':2]  # 使用标签索引中范围索引
#
# # 获取索引，和索引值
# print dat1.values
# print dat2.index
# print dat1.head(2)
#
# # 设置Series的index和values名----之后将其转换为array
# dat1.name = 'year'
# dat1.index.name = 'index'
# print dat1.head()
#
# # 对Series的过滤操作
# print dat1[dat1 > 8]
# # 对Series 做矢量运算
# print dat1 * 2
# ***********************************************************
# DataFrame
# 使用array生成DataFrame
array = np.random.rand(5, 4)
df1 = pd.DataFrame(array)
print df1
# 通过使用dict 来创建DataFrame
dict_data = {
    'A': 1,
    'B': pd.Timestamp("20170101"),
    'C': pd.Series(1, index=list(range(4)), dtype='float64'),
    'D': np.array([3] * 4, dtype='int64'),
    'E': pd.Categorical(["java", "C++", "C#", "python"]),
    'F': "Hadoop"
}

df2 = pd.DataFrame(dict_data)
print df2

# 通过索引列获取数据
data=df2['A']
print data

# 添加索引列
df2["G"]="数据分析"
print df2

# 删除数据列
del df2['G']

print df2

# 索引对象
print type(df2.index)




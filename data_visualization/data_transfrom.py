# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

"""
   transfrom中的常规运用
"""
d1 = pd.DataFrame({'c1': ['a'] * 4 + ['b'] * 4, 'data': np.random.randint(0, 4, 8)})
print d1
# 查看在DataFrame中是否存在相同的行
print d1.duplicated()

# 删除相同行默认情况下是行中所有的列数据相同认为是相同的行，如果指定匹配列，则只要是当前指定列相同，则就将整行数据删除

print d1.drop_duplicates('data')

# 在转换中常用map 函数
s1 = pd.Series(np.random.randint(0, 10, 8))

print s1.map(lambda x: x * x)

# 数据替换函数replace,替换在series中的多个值
print s1.replace([0, 2], [-1000, 100])

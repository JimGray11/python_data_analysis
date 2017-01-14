# -*- coding:utf-8 -*-
"""
pandas的数据操作
"""
import numpy as np
import pandas as pd

# 指定列名
df1 = pd.DataFrame(np.random.rand(5, 4), columns=('a', 'b', 'c', 'd'))
dict_data = {
    'A': 1,
    'B': pd.Timestamp("20170101"),
    'C': pd.Series(1, index=list(range(4)), dtype='float64'),
    'D': np.array([3] * 4, dtype='int64'),
    'E': pd.Categorical(["java", "C++", "C#", "python"]),
    'F': "Hadoop"
}
ser = pd.Series(range(5), index=('a', 'b', 'c', 'd', 'e'), dtype='int32')

df2 = pd.DataFrame(dict_data)
# dataFrame 的不联系索引
print df2['A']
print df2[['A', 'B']]

# 通过标签索引
print ser.loc[['a', 'c', 'd']]
print ser.iloc[0]
# 使用混合索引
print df2.ix[:, 'A':'D']

print df1.head()

# 在dataFrame中如果使用的是标签索引------返回的是Series,如果使用的位置索引----返回的是DataFrame
print df1['a']
print df1[[0]]

# 指定使用标签索引
print df2.loc[0:2, 'A':'D']

# 　运算与对齐
s1 = pd.Series(range(1, 10), index=range(9))
s2 = pd.Series(range(30, 36), index=range(6))
print s1 + s2

d1 = pd.DataFrame(np.ones((2, 2)), columns=('a', 'b'))
# 把相同列名的相加
d2 = pd.DataFrame(np.zeros((3, 3)), columns=('a', 'b', 'c'))

d3 = d1 + d2
print  d3
# 将nan 使用值来填充
print d3.fillna(100)

# 对不相匹配的数使用相应的值进行填充
s3 = s1.add(s2, fill_value=0)
# print  s3

# pandas 对函数的运用
d4 = pd.DataFrame(np.random.rand(3, 4) - 1, dtype='float64')
print d4

# 默认选取出每一个列中的最大值
f = lambda x: x.max()

print d4.apply(f)
# 如果需要选择一行中最大值需要，则需要选中轴方向
print  d4.apply(f, axis=1)

# 现在需要指定将否点数保留成两位小数
f2 = lambda x: '%.2f' % x

print d4.applymap(f2)

# 排序操作
s4 = pd.Series(range(10, 16), index=np.random.randint(9, size=6))
# 对Series的下标进行排序
print s4.sort_index()

d5 = pd.DataFrame(np.random.rand(3, 4), index=np.random.randint(4, size=3), columns=np.random.randint(5, size=4))
# 在dataFrame 中默是对列索引排序，如果是对行行索引排序则需要指定axis=1
# print d5.sort_index(ascending=False)
#
# print d5.sort_index()

# 需要对DataFrame中的值进行排序
# print d5.sort_values(by=2)

# 处理缺失值的方法
df_data = pd.DataFrame([np.random.randn(3), [1., np.nan, np.nan],
                       [4., np.nan, np.nan], [1., np.nan, 2.]])


print d3.isnull()

print df_data
# 默认是将带有nan 的整行数据都进行删除axis=1 表示将整列数据删除
print df_data.dropna()
print d3.fillna(100)
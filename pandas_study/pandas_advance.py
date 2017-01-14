# -*- coding:utf-8 -*-
"""
 pandas的层级索引
 数据的分组与聚合
 数据的分组运算
 pandas的透视表和交叉表
"""
import pandas as pd
import numpy as np

# 创建一个指定索引的序列
ser_obj = pd.Series(np.random.randn(12), index=[['a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c'],

                                                [0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3]])
# multiIndex多层索引对象
print ser_obj.index

# 多层索引对象的变量

print ser_obj['a']

# 内层索引的选取
print ser_obj[:, 0]

# 交换层级,并排序分层
ser_obj_swap = ser_obj.swaplevel().sort_index()
print ser_obj_swap.index

################ 数据的分组与聚合 ###################
dict_obj = {'key1': ['a', 'b', 'a', 'b',
                     'a', 'b', 'a', 'a'],
            'key2': ['one', 'one', 'two', 'three',
                     'two', 'two', 'one', 'three'],
            'data1': np.random.randn(8),
            'data2': np.random.randn(8)}
df_obj = pd.DataFrame(dict_obj)

# dataFrame 根据列名进行分组
print type(df_obj.groupby('key1')['data1'])  # 形成DataFrameGroupBy对象

# 列根据列来分组
group1 = df_obj['data2'].groupby(df_obj['key1'])

# 对分组进行运算
print group1.size()

# 按照自定义serises进行分组
sef_di_ser = pd.Series(['1', '2', '3', '1', '2', '3', '1', '2'])

group2 = df_obj['data1'].groupby(sef_di_ser)

print group2.size()

# 对多层索引使用分组

group3 = df_obj.groupby(['key1', 'key2'])

# 自定义Series 实现多层分组
group3 = df_obj.groupby([df_obj['key1'], df_obj['key2']])
# 使用unstack 使得结果更容易读
print group3.mean().unstack()

# groupby对象分组迭代-----单层索引
for group_key, group_value in df_obj.groupby(['key1']):
    print group_key
    print group_value
# groupby 对象分组迭代----多层索引

for group_key_tup, group_value in group3:
    print group_key_tup
    print group_value

# 将group 对象转换为list
print list(df_obj.groupby(['key1']))

# 在转换为dict必须先转换为list
print dict(list(df_obj.groupby(['key2'])))

# 按照列进行分组-------把相同的列放在一起

print df_obj.groupby(df_obj.dtypes, axis=1).sum()

# 自定义列分组
mapping_dict = {'key1': 0, 'key2': 1, 'data1': 2, 'data2': 2}

print df_obj.groupby(mapping_dict, axis=
1).sum()

# 通过索引级别进行分组
multiIndex = pd.MultiIndex.from_arrays([['Python', 'Java', 'Python', 'Java', 'Python'],
                                        ['A', 'A', 'B', 'C', 'B']], names=['language', 'index'])
df_obj4 = pd.DataFrame(np.random.randint(1, 5, (5, 5)), columns=multiIndex)
# 根据language进行分组
print df_obj4.groupby(level='language', axis=1).sum()

###########################---聚合操作-----##############
dict_obj = {'key1': ['a', 'b', 'a', 'b',
                     'a', 'b', 'a', 'a'],
            'key2': ['one', 'one', 'two', 'three',
                     'two', 'two', 'one', 'three'],
            'data1': np.random.randint(1, 10, 8),
            'data2': np.random.randint(1, 10, 8)}

df_obj4 = pd.DataFrame(dict_obj)


# 自定义聚合函数
def max_sub_min(df):
    return df.max() - df.min()


print df_obj4.groupby('key1').agg(max_sub_min)

# 一次分组同时同时进行多种计算
print df_obj4.groupby('key2').agg(['mean', 'sum', 'std', ("diff_ms", max_sub_min)])

# 需要对分组中的不同组进行不同的计算
map_dict = {'data1': ['mean', 'max'],
            'data2': 'min'}
print df_obj4.groupby('key2').agg(map_dict)

# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

"""
主要是了解numpy、Series、和DataFrame 的contact之间的不同之处
"""
# 1 在numpy中的合并
# arr1 = np.random.randint(0, 10, (3, 4))
# arr2 = np.random.randint(10, 20, (2, 4))

# 注意在numpy 中需要使得合并的相关轴的维度一致
# print np.concatenate([arr1, arr2])
# 2 在Series 中的合并--不需要相关轴一致，如果不相同会使用NaN来进行填充
# 2.1 在index 没有重复的情况
s1 = pd.Series(np.random.randint(0, 5, 5), index=range(0, 5))
s2 = pd.Series(np.random.randint(0, 8, 3), index=range(5, 8))
s3 = pd.Series(np.random.randint(0, 12, 4), index=range(8, 12))

# print pd.concat([s1, s2, s3], axis=1)
# 2.2 在index 上存在重复的情况----是取出所有Series的index的并集作为index 没有数的使用NaN来填充

s1 = pd.Series(np.random.randint(0, 5, 5), index=range(0, 5))
s2 = pd.Series(np.random.randint(0, 8, 3), index=range(0, 3))
s3 = pd.Series(np.random.randint(0, 12, 4), index=range(0, 4))
# print pd.concat([s1, s2, s3], axis=1)
# 2.3 如果是根据index的交集来取数据，需要使用jion来指定
# print pd.concat([s1, s2, s3], axis=1, join='inner')
# 对于DataFrame的contact默认是对列和index都取并
d1 = pd.DataFrame(np.random.randint(0, 10, (3, 4)), index=range(3), columns=['A', 'B', 'C', 'D'])
d2 = pd.DataFrame(np.random.randint(0, 10, (2, 4)), index=range(3, 5), columns=['A', 'B', 'C', 'E'])

print pd.concat([d1, d2], axis=1)

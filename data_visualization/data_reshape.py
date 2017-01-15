# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

"""
主要是让现有的DataFrame 调整结构
"""
# 使用stack 将DataFrame 调整为Series
d1 = pd.DataFrame(np.random.randint(0, 10, (3, 2)), index=range(3), columns=['A', 'B'])
# 调用stack()方法之后，将DataFrame 对应的columns转换为内存索引
stacked = d1.stack()
print stacked.index
print type(stacked)

# 使用unstack方法，将MultiIndex多层索引的Series转换为DataFrame,默认是将level=1 转换DataFrame中的列
print stacked.unstack(level=1)

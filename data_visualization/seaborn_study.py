# -*- coding:utf-8 -*-
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

"""
 主要是了解seaborn的常规使用
 seaborn的特点：
    多个内置主题和颜色主题
    可用于单一变量和二维变量用于比较数据集中各个变量之间的分布关系
    可视化线性回归中的独立变量和不独立变量
    可视化矩阵数据，通过矩阵聚类算法探究矩阵间的结构
    可视化时间序列数据以及不确定的展示
    可分割区域制图，展示复杂的可视化
"""
# 数据集分布可视化----单变量分布
# x1 = np.random.normal(size=500)
# sns.distplot(x1)
# ----------单变量分布-------
x1 = np.random.normal(size=500)
# sns.distplot(x1)
# 显示画的图
# 如果不需要拟合的曲线则设置kde=False
# 画出直方图
x2 = np.random.randint(0, 100, 500)
# sns.distplot(x2, kde=False, rug=True)
# 核密度估计-----只有曲线,设置hist=False或者使用sns.keplot()
# sns.distplot(x2,hist=False,rug=True)
# sns.kdeplot(x2,shade=True)
# sns.rugplot(x2)
# 拟合参数估计
# sns.distplot(x1, kde=False, fit=stats.gamma)

# 双变量分布
d1 = pd.DataFrame({'x': np.random.randn(500),
                   'y': np.random.randn(500)})
d2 = pd.DataFrame({'x': np.random.randn(500),
                   'y': np.random.randint(0, 100, 500)})
# sns.jointplot(x='x', y='y', data=d1)
# 二维直方图
# sns.jointplot(x='x',y='y',data=d2,kind='hex')
# 核密度估计
# sns.jointplot(x='x',y='y',data=d2,kind='kde')

# 数据集中变量间关系可视化
dataset = sns.load_dataset("tips")
# dataset = sns.load_dataset("iris")
sns.pairplot(dataset)
sns.plt.show()

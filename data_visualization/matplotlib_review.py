# -*- coding:utf-8 -*-
"""
主要是对matlibplot 画图的总结
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 在matplotlib 中的颜色、标记和线型
# -------颜色------
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white
# ------标记------
# ”.” 	point
# ”,” 	pixel 表示像素
# “o” 	circle
# “v” 	triangle_down
# “^” 	triangle_up
# “<” 	triangle_left
# ------线型------
# linestyle 	description
# '-' or 'solid' 	solid line
# '--' or 'dashed' 	dashed line
# '-.' or 'dashdot' 	dash-dotted line
# ':' or 'dotted' 	dotted line
# 'None' 	draw nothing
# ' ' 	draw nothing
# '' 	draw nothing
fig, axes = plt.subplots(2)

axes[0].plot(np.random.randint(0, 100, 50), 'ro--')
# 等价于
axes[1].plot(np.random.randint(0, 100, 50), color='r', linestyle='dashed', marker='o')
# plt.show()

# 刻度、标签、图例
# ----设置刻度范围----
# plt.xlim(),plt.ylim()
# ax.set_xlim() ax.set_ylim()
# ------设置显示的刻度-----
# ax.set_xticks() ax.set_yticks()
# -----设置刻度标签-----
# ax.set_xticklabels() ax.set_yticklabels()
# ---- 设置坐标轴标签-----
# ax.set_xlabel() ax.set_ylabel()
# ----设置标题----
# ax.set_title()
# ----设置图例----
# ax.plot(label='sum')
# ax.legend() ----loc='best'

# 在ax上作图
fig, ax = plt.subplots(1)
ax.plot(np.random.randn(1000).cumsum())
# 设置刻度范围
ax.set_xlim([0, 800])
# 设置显示刻度
ax.set_xticks(range(0, 500, 100))
# 设置刻度标签
ax.set_yticklabels(['Jan', 'Feb', 'Mar'])
# 设置轴标签
ax.set_xlabel('Number')
ax.set_ylabel('Month')
# 设置标题
ax.set_title('examples')
# 在画图时显示图例
ax.plot(np.random.randn(1000).cumsum(), label='line1')
ax.plot(np.random.randn(1000).cumsum(), label='line2')
ax.legend(loc='best')

plt.show()

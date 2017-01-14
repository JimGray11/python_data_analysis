#!/usr/bin/env python
import numpy as np
import datetime
import matplotlib.pyplot as plt

'''
@project name :2016美国总统大选民意调查分析
@project target: 分析出每个月的民意调查结果
@author :ywendeng
@date:2016/12/18
'''


def data_extract_transform():
    # 从本地读取csv源数据文件
    fname_dir = "C:\\Users\\JimG\\Desktop\\数据科学电子书\\数据分析\\codes\\presidential_polls.csv"
    # 在loadtxt中,指定需要获取的列，必须为下标，所以需要先获取到上述列在文件中的下标位置

    # 表示需要选取的数据列
    uscols_name = ("enddate", "rawpoll_clinton", "rawpoll_trump", "adjpoll_clinton", "adjpoll_trump")

    with open(fname_dir, "r") as f:
        line = f.readline()[:-1]  # -1表示不读取每行末尾的\n 换行符
        col_name_list = line.split(",")
    # 根据列名得到列在文件中对应的位置
    uscols_sub_num_list = [col_name_list.index(name) for name in uscols_name]
    data = np.loadtxt(
        fname=fname_dir,
        dtype=bytes,
        delimiter=",",
        skiprows=1,
        usecols=uscols_sub_num_list
    ).astype(str)
    # 在enddate列中存在格式为9-10-2016格式的数据,data为数组
    endtime_idx = uscols_name.index("enddate")
    endtime_list = data[:, endtime_idx].tolist()

    endtime_format = [endtime.replace("-", "/") for endtime in endtime_list]
    # 将日期字符串，转换为日期
    # print(endtime_format)

    date_lst = [datetime.datetime.strptime(end, '%m/%d/%Y') for end in endtime_format]
    # 构造年份-月份列表
    month_lst = ["%d-%02d" % (dt.year, dt.month) for dt in date_lst]
    # 将列表转换为ndarray 数组(矩阵)------具有适量运算能力
    month_array = np.array(month_lst)
    # 取出唯一的年-月份
    moths = np.unique(month_array)
    rawpoll_clinton_idx = uscols_name.index("rawpoll_clinton")
    # 一个人对应的所有数据
    rawpoll_clinton_data = data[:, rawpoll_clinton_idx]

    rawpoll_trump_idx = uscols_name.index("rawpoll_trump")
    # 一个人对应的所有数据
    rawpoll_trump_data = data[:, rawpoll_trump_idx]

    adjpoll_clinton_idx = uscols_name.index("adjpoll_clinton")
    adjpoll_clinton_data = data[:, adjpoll_clinton_idx]

    adjpoll_trump_idx = uscols_name.index("adjpoll_trump")
    adjpoll_trump_data = data[:, adjpoll_trump_idx]

    results = []
    for moth in moths:
        # 使用条件索引,得到每个月相应的数据
        rawpoll_cliton_month_data = rawpoll_clinton_data[month_array == moth]
        rawpoll_cliton_month_sum = get_sum(rawpoll_cliton_month_data)

        rawpoll_trump_month_data = rawpoll_trump_data[month_array == moth]
        rawpoll_trump_month_sum = get_sum(rawpoll_trump_month_data)

        adjpoll_clinton_month_data = adjpoll_clinton_data[month_array == moth]
        adjpoll_clinton_month_sum = get_sum(adjpoll_clinton_month_data)

        adjpoll_trump_month_data = adjpoll_trump_data[month_array == moth]
        adjpoll_trump_month_sum = get_sum(adjpoll_trump_month_data)
        # 将每个月中每个人的民调总数加入到列表中
        results.append((moth, rawpoll_cliton_month_sum, rawpoll_trump_month_sum, adjpoll_clinton_month_sum
                        , adjpoll_trump_month_sum))

    return results


def data_view(result):
    month, raw_cliton_sum, raw_trump_sum, adj_clinton_sum, adj_trump_sum = zip(*result)
    fig, subpolt = plt.subplots(2, 2, figsize=(15, 20))
    # 画出折线图
    subpolt[0, 0].plot(raw_cliton_sum, color='r')
    subpolt[0, 0].plot(raw_trump_sum, color='g')
    # 画出直方图
    width = 0.25
    # 设置横坐标范围
    x = np.arange(len(month))
    subpolt[0, 1].bar(x, adj_clinton_sum, width, color='y')
    subpolt[0, 1].bar(x + width, adj_trump_sum, width, color='b')
    # 设置下标的宽度和标记
    subpolt[0, 1].set_xticks(x + width)
    subpolt[0, 1].set_xticklabels(month, rotation="vertical")

    # 调整数据趋势展示
    subpolt[1, 0].plot(adj_clinton_sum, color='y')
    subpolt[1, 0].plot(adj_trump_sum, color='b')

    # 原始数据的柱状图展示
    subpolt[1, 1].bar(x, raw_cliton_sum, width, color='r')
    subpolt[1, 1].bar(x + width, raw_trump_sum, width, color='g')
    subpolt[1, 1].set_xticks(x + width)
    subpolt[1, 1].set_xticklabels(month, rotation="vertical")
    plt.show()


def get_sum(data):
    # 从python3.3 之后filter 返回filter object 是一个iterable对象
    filter_data = [item for item in filter(is_float, data)]
    # 将数据转换为float 类型的数组
    float_filter_data = np.array(filter_data, np.float)
    return np.sum(float_filter_data)


def is_float(x):
    try:
        float(x)
    except:
        return False
    else:
        return True


if __name__ == "__main__":
    result = data_extract_transform()
    data_view(result)

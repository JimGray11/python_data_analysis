# -*- coding:utf-8 -*-
"""
0.数据的转换
1.分析空难vs年份之间的关系
2.分析乘客数量vs遇难人数vs年份之间的关系
3.分析空难数前20的机型
4.分析空难数前20的operator
"""
import pandas as pd
from pandas_tools import inspect_data,process_missing_data,convert_data_time,\
    plot_crashes_vs_year

def run_main():
    df_data=pd.read_csv('./dataset/Airplane_Crashes_and_Fatalities_Since_1908.csv')
    # 查看数据的基本信息
    inspect_data(df_data)
    # 使用0来填充缺失的数据
    df_data=process_missing_data(df_data)
    # 统一date 列的时间格式，同时在数据集中添加单独的一列year
    df_data=convert_data_time(df_data)
    # 对每年空难数的统计
    plot_crashes_vs_year(df_data,'bokeh')
    return None


if __name__ == '__main__':
    run_main()

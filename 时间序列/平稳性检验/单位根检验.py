# 3.单位根检验：Dickey-Fuller test
# 单位根检验是指检验序列中是否存在单位根，如果存在单位根，那就是非平稳时间序列。

from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np

df = pd.read_csv("../production.csv")
data = np.array(df["production"].values)
result = adfuller(data)
output = {'Test Statistic Value': result[0],
          'p-value': result[1],
          'Lags Used': result[2],
          'Number of Observations Used': result[3],
          'Critical Value(1%)': result[4]['1%'],
          'Critical Value(5%)': result[4]['5%'],
          'Critical Value(10%)': result[4]['10%']}
print(output)
# 返回结果:
# Test Statistic Value: 统计值
# p-value: t统计量对应的概率值，p值要小于给定的显著性水平才可以拒绝假设
# p值越接近零越好
# 如果p_value接近于 0.05 时，则要通过临界值(Test Statistic Value 和 Critical Value)进行判断
# Lags Used: 滞后阶数
# Number of Observations Used: 统计的数据的数目
# Critical Value(1%, 5%, 10%): 不同程度拒绝原假设的统计值
# ADF检验的原假设是存在单位根，
# 只要这个统计值是小于 1%水平下的数字就可以极显著的拒绝原假设，认为数据平稳
# 注意，ADF值一般是负的，也有正的，但是它只有小于1%水平下的才能认为是及其显著的拒绝原假设

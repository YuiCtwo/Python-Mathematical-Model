# python 假设检验例子

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats

# stats 是统计学的包
# 文档: https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
# 数据链接 test.csv
# 一些常见的缩写
# rvs: Random Variates
# pdf: Probability Density Function                         概率密度函数
# cdf: Cumulative Distribution Function                     概率密度函数的积分函数
# ppf: Percent Point Function (Inverse of CDF)              百分点函数，概率密度函数的积分值
"""
解决问题
1.人体体温的总体均值是否为98.6华氏度?
2.人体的温度是否服从正态分布?
3.人体体温中存在的异常数据是哪些?
4.男女体温是否存在明显差异?
5.体温与心率间的相关性(强/弱/中等?)
"""

test_df = pd.read_csv("test.csv")
alpha = 0.05  # 显著性水平
# 1 假设 mu=98.6 计算 z检验
mu = 98.6
temperature_data = test_df["Temperature"]
sample_mean = np.mean(temperature_data)  # 计算样本均值
# numpy.std() 求标准差的时候默认是除以 n 的，即是有偏的, np.std无偏样本标准差方式为加入参数 ddof = 1
# pandas.std() 默认是除以 n-1 的, 即是无偏的，加上参数 ddof=0, 可得有偏方差
sample_std = np.std(temperature_data, ddof=1)  # 计算样本方差
sample_size = temperature_data.size
# z = (sample_mean - mu) / (sample_std / np.sqrt(sample_size))
# print(z)
#
# # 直接调用 statsmodels包函数计算
# result = weightstats.ztest(x1=temperature_data,  # 变量 1
#                            x2=None,              # 变量 2
#                            value=sample_size,    # X1的零假设下的平均
#                            alternative="two-sided",  # 双边检验
#                            usevar='pooled',
#                            ddof=1)
#
# print(result)

# 2 验证是否符合正态分布(K-S 检验)
# k_result = stats.kstest(temperature_data, 'norm')
# print(k_result)  # p_value < 0.05 拒绝假设(置信度为 0.05)
#
# # 检验是否符合 t分布
# # 先用 t分布拟合区域收入均值，然后使用 ks_2samp函数比较区域收入均值和 t分布的随机变量
# ks = stats.t.fit(temperature_data)
# df = ks[0]
# loc = ks[1]
# scale = ks[2]
# t_estimate = stats.t.rvs(df=df, loc=loc, scale=scale, size=sample_size)
# t_result = stats.ks_2samp(temperature_data, t_estimate)
# print(t_result)  # p_value > 0.05 服从t 分布
#
# 校验是否符合卡方分布
# chi_square = stats.chi2.fit(temperature_data)
# df = chi_square[0]  # df: 自由度
# loc = chi_square[1]
# scale = chi_square[2]
# chi_estimate = stats.chi2.rvs(df=df, loc=loc, scale=scale, size=sample_size)
# chi_result = stats.ks_2samp(temperature_data, chi_estimate)
# print(chi_result)  # p_value > 0.05 服从卡方分布(数值更大，说明更加符合卡方分布)

# 3
# 在得到体温数据的情况下，可以计算 p=0.025和 p=0.925时的分布值，
# 在分布值两侧的数据属于小概率，可以认为是异常值
# chi2_distribution = stats.chi2(chi_square[0], chi_square[1], chi_square[2])  # 构建卡方分布
# left_limit = chi2_distribution.ppf(0.025)
# right_limit = chi2_distribution.ppf(0.925)
# print(temperature_data[temperature_data > right_limit])
# print(temperature_data[temperature_data < left_limit])

# 4 两个总体均值之差的假设检验问题
# data_size = test_df.groupby(['Gender']).size()
# male_df = test_df.loc[test_df["Gender"] == 1]
# female_df = test_df.loc[test_df["Gender"] == 2]
#
# stat, p = stats.ttest_ind(male_df['Temperature'], female_df['Temperature'])
# print('stat=%.3f, p=%.3f' % (stat, p))
# # 内置的置信度都是 0.05
# if p > 0.05:
#     print("不能拒绝原假设，男女体温无明显差异。")
# else:
#     print("拒绝原假设，男女体温存在明显差异。")

# 5 使用皮尔逊相关系数检验数据的相关性
heart_rates = test_df["HeartRate"]
temperatures = test_df["Temperature"]
stat, p = stats.pearsonr(heart_rates, temperatures)
# >0 表示有正相关性, =1表示完全相关
print('stat=%.3f, p=%.3f' % (stat, p))

# Q-Q图 (Quantity-Quantile Plot)
# Q-Q图通过把测试样本数据的分位数与已知分布相比较，从而来检验数据的分布情况
# Q-Q图是一种散点图，对应于正态分布的QQ图，就是由标准正态分布的分位数为横坐标，样本值为纵坐标的散点图

# 绘制思路
# 1在做好数据清洗后，对数据进行排序次序统计量：x(1)<x(2)<....<x(n)
# 2排序后，计算出每个数据对应的百分位 p{i}，即第 i个数据 x(i)为 p(i)分位数，其中 p(i)=(i-0.5)/n （pi有多重算法，这里以最常用方法为主）
# 3绘制直方图 + qq图，直方图作为参考

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 使用 Q-Q图来检验是否符合温度正态分布
from scipy import stats

data = pd.read_csv("test.csv")
temperature_data = data["Temperature"]

# 直接调用库计算
stats.probplot(temperature_data, dist="norm", plot=plt)
plt.show()

# 按照计算步骤计算
size = temperature_data.size
mean = temperature_data.mean()
std = temperature_data.std()
print('均值为：%.2f，标准差为：%.2f' % (mean, std))
print('------')
df = pd.DataFrame(temperature_data.values, columns=["value"])
# df.sort_values(by="value", inplace=True)  # 重新排序
# print(df.head())
# temperature_data_r = df.reset_index(drop=False)  # 重新排序后，更新 index
# print("----------\n", temperature_data_r.head())
# # 计算经验分布函数的分位数和理论分布的函数的分位数
# temperature_data_r['z_alpha'] = (temperature_data_r.index - 0.5) / size
# temperature_data_r['p'] = (temperature_data_r['value'] - mean) / std  # 标准正态化
# temperature_data_r['q'] = stats.norm.ppf((temperature_data_r.index - 0.5) / size, 0, 1)  # yi = f^-1((i-0.5)/n)
# print(temperature_data_r.head())
# fig = plt.figure(figsize=(10, 9))
# ax1 = fig.add_subplot(3, 1, 1)  # 创建子图1
# ax1.scatter(df.index, df.values)
# plt.grid()
# # 绘制数据分布图

# ax2 = fig.add_subplot(3, 1, 2)  # 创建子图2
# df.hist(bins=30, alpha=0.5, ax=ax2)
# df.plot(kind='kde', secondary_y=True, ax=ax2)
# plt.grid()
# 绘制直方图

# 绘制QQ图，直线为四分之一位数、四分之三位数的连线，基本符合正态分布
# ax3 = fig.add_subplot(3, 1, 3)  # 创建子图3
# ax3.plot(temperature_data_r['q'], temperature_data_r['p'], 'ko')
# x = np.arange(-2.5, 3.5, 0.01)
# ax3.plot(x, x, 'r-')
# plt.grid()
#
# plt.show()

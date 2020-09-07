# 1.时序图检验：
# 根据平稳时间序列的均值和方差都是常数的特性，平稳序列的时序图显示该序列值时钟在一个参数附近随机波动，而且波动的范围是有界的。
# 如果有明显的趋势或者周期性， 那它通常不是平稳序列
# 简单来说就是看图来判断是否是平稳的
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../production.csv", index_col="year")
df.index = pd.to_datetime(df.index, format="%Y")  # format:指定日期的格式
df.plot()
plt.show()
# 2.自相关图检验：
# 平稳序列具有短期相关性，通常只有近期的序列值得影响比较明显，间隔越远的过去值对现在的值得影响越小。
# 而非平稳序列的自相关系数衰减的速度比较慢
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../production.csv", index_col="year")
df.index = pd.to_datetime(df.index, format="%Y")

plot_acf(df)  # 自相关图
# 置信区间为蓝色背景，默认情况下是 95%
# 横坐标是延迟 k, 纵坐标是相关性, 表示相距 k个时间间隔的序列(延迟值为 k)数据之间的相关性
# 其实自相关系数可以这么理解：把一列数据按照滞后数拆成两列数据，在对这两列数据做类似相关系数的操作
# 1-6 3-10 2组，这样滞后系数就是 2，2列数据的相关系数就是滞后系数为 2的自相关系数
# plot_pacf(df)  # 偏相关图
plt.show()
# -*- coding:utf-8 -*-
from scipy.stats import binom, norm, beta, expon
import numpy as np
from matplotlib import pyplot as plt
# 概率分布的模型

# 常见的分布还有 f: F分布, t: 学生 T分布
# 二项分布
# n表示 n次重复独立试验
# p表示事件 A出现的概率
# size表示做多少次二项分布试验
# rvs: 产生服从指定分布的随机数
binom_data = binom.rvs(n=10, p=0.5, size=10000)
# std: 标准差
# mean: 平均值
print("Mean: %g" % np.mean(binom_data))
print("SD: %g" % np.std(binom_data, ddof=1))
plt.hist(binom_data, density=True)
plt.xlabel('x')
plt.ylabel("density")

plt.show()

# -*- coding:utf-8 -*-

from scipy.stats import binom, norm, beta, expon
import numpy as np
from matplotlib import pyplot as plt
# 泊松分布
plt.subplot(121)
x = np.random.poisson(lam=5, size=10000)
pillar = 15
# range:设置显示的范围,范围之外的将被舍弃
# normed: 归一化处理(求频率)
# bins: 图中的柱的个数
frequency, bins, col_lists = plt.hist(x, bins=pillar, range=[0, pillar], color='g', alpha=0.5, density=True)
# hist()第一个返回值是统计各个区间的频数，第二个返回值是 bins
for i in range(1, pillar+1):
    if frequency[i-1] <= 0.02:
        pass
    else:
        plt.text(i - 1 + 1/2, frequency[i-1] + 0.002, "%.3f" % frequency[i-1], fontsize=5)

plt.plot(bins[0: pillar] + 1/2, frequency, 'r')
# 显示网格线
plt.grid()

# 指数分布
plt.subplot(122)
lam = 0.5
x = np.arange(0, 15, 0.1)
y = expon.pdf(x, lam)
plt.plot(x, y)
plt.title("Exponential: lam=%.2f" % lam)
plt.xlabel('x')
plt.ylabel("density")

plt.show()
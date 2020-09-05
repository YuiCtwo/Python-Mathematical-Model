# -*- coding:utf-8 -*-
from scipy.stats import binom, norm, beta, expon
import numpy as np
from matplotlib import pyplot as plt
# 正态分布
plt.subplots(221)
mu = 0
sigma = 1
x = np.arange(-5, 5, 0.1)
# pdf: 在 x处的概率密度函数 f(x)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel("density")
plt.show()
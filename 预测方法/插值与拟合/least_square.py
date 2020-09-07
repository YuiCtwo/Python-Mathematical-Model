# -*- coding:utf-8 -*-
# 最小二乘法

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
a, b, c = 1, 2, 3
y_exact = a + b * x + c * x ** 2

# 构造随机的散点
m = 100
xi = 1 - 2 * np.random.rand(m)
print("xi.shape", xi.shape, xi ** 1, xi)
yi = a + b * xi + c * xi ** 2 + np.random.randn(m)
# A = [1, xi, xi^2] 是 n x 3 的矩阵
A = np.vstack([xi**0, xi**1, xi**2])
sol, r, rank, s = linalg.lstsq(A.T, yi)
# 最小二乘法得到的函数
y_fit = sol[0] + sol[1] * x + sol[2] * x ** 2
fig, ax = plt.subplots(figsize=(12, 4))
# alpha: 线的明暗程度
ax.plot(xi, yi, "go", alpha=0.5, label="Simulated data")
# k: 黑色 lw: line width, 线条宽度
ax.plot(x, y_exact, 'k', lw=2, label="True value $y = 1 + 2x + 3x^2$")
ax.plot(x, y_fit, 'b', lw=2, label="Least square fit")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc=2)
plt.show()

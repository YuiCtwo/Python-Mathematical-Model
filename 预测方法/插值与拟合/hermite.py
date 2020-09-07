# -*- coding:utf-8 -*-

# 埃尔米特插值
from scipy.interpolate import KroghInterpolator
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 + 1


xs = np.linspace(-5, 5, 100)
nodes = np.array([0, 1, 2, 3])
xi = np.array([0, 1, 2, 3])
yi = np.array([1, 2, 9, 28])
interpolant = KroghInterpolator(xi, yi)
plt.figure()

plt.subplot(121)
plt.plot(xs, interpolant(xs), "b--", label="Hermite interpolation")
plt.plot(nodes, f(nodes), "ro", label="nodes")
# 显示图中的标签
plt.legend(loc=9)
# 设定坐标上下限
plt.xlim(-10.5, 10.5)
plt.title("$f(x) = x^3 + 1$")
# 1行 2列
plt.subplot(122)
plt.plot(xs, f(xs), "g--", label="original")
plt.plot(xi, f(xi), "ro", label="nodes")
plt.legend(loc=9)
plt.title("$f(x) = x^3 + 1$")
plt.xlim(-10.5, 10.5)
plt.show()
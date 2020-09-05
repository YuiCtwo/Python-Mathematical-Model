# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import lagrange
"""
4.17952x^3 + -13.9064x^2 + 22.9034x^1 + -16.2281
1 + 1.93311x^1 + -1.06036x^2 + 0.845536x^3
"""


def f(x):
    return math.e ** x


def f_lagrange(x):
    return 4.17952*x**3 - 13.9064*x**2 + 22.9034*x - 16.2281


def f_newton(x):
    return 1 + 1.93311*x**1 - 1.06036*x**2 + 0.845536*x**3


# f_lagrange = lagrange([0, 1, 2, 3], [math.e**y for y in range(4)])
# print(f_lagrange)
xs = np.linspace(0, 5, 50)
ys = [f(x) for x in xs]
ys_lagrange = [f_lagrange(x) for x in xs]
ys_newton = [f_newton(x) for x in xs]
plt.plot(xs, ys, "r-", label="original:e^x")
plt.plot(xs, ys_lagrange, "b--", label="lagrange_insertion")
plt.plot(xs, ys_newton, "g:", label="newton_insertion")
plt.legend(loc="best")
plt.show()
plt.savefig("./d.png")

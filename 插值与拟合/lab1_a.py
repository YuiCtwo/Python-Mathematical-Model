# -*- coding:utf-8 -*-

from scipy.interpolate import lagrange
import math
import matplotlib.pyplot as plt
import numpy as np


# 验证拉格朗日插值对于不同函数的插值效果
def f1(x):
    return math.e ** x


def f2(x):
    return x**3 - 10*x**2 + 19.68*x - 10.944


# xs = [1, 2, 3, 4]
# y_f1 = [f1(x) for x in xs]
# f = lagrange(xs, y_f1)
# y_f1 = [f2(x) for x in xs]
# f = lagrange(xs, y_f1)

x_draw = np.linspace(0, 8, 100)
# y_draw = f(x_draw)
# y_origin = [f1(x) for x in x_draw]
y_origin = [f2(x) for x in x_draw]
# plt.plot(x_draw, y_draw, "g--", label="lagrange insertion")
plt.plot(x_draw, y_origin, label=r"$y=x^3-10x^2+19.68x-10.944$")
plt.xticks(np.linspace(1, 8, 8))
plt.plot(x_draw, np.linspace(0, 0, 100),  "g--")
plt.legend()
# plt.savefig("./lab1_a_1.png")
plt.savefig("./lab1_a_3.png")
plt.show()



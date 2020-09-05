# -*- coding:utf-8 -*-
from scipy.interpolate import lagrange
import math
import matplotlib.pyplot as plt
import numpy as np


# 验证拉格朗日插值对于不同插值点个数的插值效果
def f(x):
    return math.sin(x)


xs = [0, 1, 3, 5]
y_f2 = [f(x) for x in xs[0:3]]
y_f3 = [f(x) for x in xs[0:4]]
f2 = lagrange(xs[0:3], y_f2)
f3 = lagrange(xs[0:4], y_f3)

x_draw = np.linspace(0, 10, 50)
y_draw2 = f2(x_draw)
y_draw3 = f3(x_draw)
y_origin = [f(x) for x in x_draw]
plt.plot(x_draw, y_draw2, "r--", label="lagrange insertion:point 3")
plt.plot(x_draw, y_draw3, "c-", label="lagrange insertion:point 4")
plt.plot(x_draw, y_origin, "b:", label="y=sin(x)")
plt.legend()
plt.savefig("./lab1_b_3.png")
plt.show()



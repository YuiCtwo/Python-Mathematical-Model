# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep


# 一元样条插值
def f1(x):
    return x ** 2 + 10 * np.sin(x) + 1
x = np.linspace(0, 10, 20)
y = f1(x)
plt.plot(x, y, "*-")
plt.show()

x2 = np.linspace(0, 10, 200)
# splrep()计算出b样条曲线的参数tck
spl = splrep(x, y, s=0)
y2 = splev(x2, spl)
# 多条线一起画
plt.plot(x, y, 'o', x2, y2)
plt.show()
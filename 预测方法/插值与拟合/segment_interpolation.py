# -*- coding:utf-8 -*-
# 分段线性插值
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pylab as pl

x = np.linspace(0, 10, 101)
y = np.sin(x)
x_new = np.linspace(0, 10, 11)
pl.plot(x, y)

kind = "slinear"
f = interpolate.interp1d(x, y, kind=kind)
y_new = f(x_new)
pl.plot(x_new, y_new, label=kind)
pl.legend("best")
pl.show()

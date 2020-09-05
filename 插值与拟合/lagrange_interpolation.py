# -*- coding:utf-8 -*-

# 拉格朗日插值
from scipy.interpolate import lagrange

x = [1, 2, 3, 4]
y = [4, 15, 41, 85]
ret = lagrange(x, y)
print(ret)
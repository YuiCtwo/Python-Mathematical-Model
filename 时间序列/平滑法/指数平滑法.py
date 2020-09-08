import numpy as np
from matplotlib import pyplot as plt


# 一次指数平滑法
def exponential_smoothing(alpha, s):
    s2 = np.zeros(s.shape)
    s2[0] = s[0]
    for i in range(1, len(s2)):
        s2[i] = alpha*s[i]+(1-alpha)*s2[i-1]
    return s2


# 二次指数平滑法
def twi_order_exponential_smoothing(alpha, s, st1_f=None, st2_f=None):
    s2 = np.zeros(s.shape)
    st1 = []
    st2 = []
    if st1_f is not None:
        st1.append(st1_f)  # 给定初始化值
    if st2_f is not None:
        st2.append(st2_f)
    s2[0] = s[0]
    for i in range(1, len(s2)):
        v1 = alpha*s[i] + (1-alpha)*st1[i-1]
        st1.append(v1)
        v2 = alpha*v1 + (1-alpha)*st2[i-1]
        s2[i] = (1+1/(1-alpha))*v1 - (1/(1-alpha))*v2
    return s2
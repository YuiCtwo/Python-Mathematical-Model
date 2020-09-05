# -*- coding:utf-8 -*-

# 黄金分割法和斐波那契法
# 求函数的近似极小点，要求缩短后的区间不大于区间 [-1, 3] 的 0.08倍

import numpy as np


def fx(x):
    return x ** 2 - x + 2


def fibonacci(x):
    if x <= 0:
        return 1
    if x == 1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)


def fibo_method(init_a, init_b, n, delta):
    k = 1
    a = init_a
    b = init_b
    t1 = a + (fibonacci(k-1) / fibonacci(k) * (b - a))
    t2 = a + (fibonacci(k-2) / fibonacci(k) * (b - a))
    while k < n-1:
        f1 = fx(t1)
        f2 = fx(t2)
        if f1 < f2:
            a = t2
            t2 = t1
            t1 = a + (fibonacci(n - 1 - k) / fibonacci(n - k)) * (b - a)
        else:
            b = t2
            t1 = t2
            t2 = b + (fibonacci(n - 1 - k) / fibonacci(n - k)) * (a - b)
        k = k + 1
    # t1 = t2 = (a + b) / 2
    t2 = (a + b) / 2
    t1 = a + (0.5 + delta) * (b - a)
    if fx(t2) < fx(t1):
        return t2, b
    else:
        return a, t1


if __name__ == "__main__":
    t = 2
    while True:
        result = fibonacci(t)
        if result >= 50:
            print(t)
            break
        else:
            t = t + 1
    res = fibo_method(-1, 3, t, 0.03)
    print(res)
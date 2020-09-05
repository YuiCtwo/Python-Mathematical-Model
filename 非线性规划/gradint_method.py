import math
import numpy as np

def f(args):
    return args[0] ** 2 + 25 * args[1] ** 2


def df(args):
    return 2 * args[0] + 50 * args[1]


def gradient_descent(x0, epsilon):
    fx = f(x0)
    dfx = df(x0)
    k = 0
    while math.fabs(dfx) > epsilon:
        # 构造负梯度方向
        pk = -dfx
        # 进行一维搜索求 tk
        t = 1
        temp = (x0[0] + t * pk, x0[1] + t * pk)
        f_value = f(temp)
        while f_value > fx:
            t = t / 2
            f_value = f((x0[0] + t * pk, x0[1] + t * pk))
        k += 1
        x0 = tuple([x + t * pk for x in x0])
        dfx = df(x0)
        fx = f(x0)

    return x0, fx, k


x, fx, turns = gradient_descent((2, 2), 0.000001)
print(x)
print(fx)
print(turns)






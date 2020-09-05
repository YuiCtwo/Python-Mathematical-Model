# -*- coding:utf-8 -*-
import time

from scipy.optimize import minimize
import numpy as np


def fx(args) -> float:
    return args[0] ** 2 + args[1] ** 2 + args[2] ** 2 + 8


# 约束条件 1
def constrain_1(args) -> float:
    return args[0] ** 2 - args[1] + args[2] ** 2


# 约束条件 2
def constrain_2(args) -> float:
    return -(args[0] + args[1] ** 2 + args[2] ** 2 - 20)


# 约束条件 3
def constrain_3(args) -> float:
    return -args[0] - args[1] ** 2 + 2


# 约束条件 4
def constrain_4(args) -> float:
    return args[1] + 2 * args[2] ** 2 - 3


# 设置初始猜测值
x0 = np.asarray((1, 1, 1))

# 边界约束
bounds = ((0, None), (0, None), (0, None))

# ineq 大于等于约束
con1 = {"type": "ineq", "fun": constrain_1}
con2 = {"type": "ineq", "fun": constrain_2}
con3 = {"type": "eq", "fun": constrain_3}
con4 = {"type": "eq", "fun": constrain_4}

cons = ([con1, con2, con3, con4])
time_SLSQT = time.time()
solution = minimize(fx, x0, bounds=bounds, constraints=cons, method="SLSQP")
print(solution.x)
print(solution.fun)
print("Use Time:", time.time() - time_SLSQT)



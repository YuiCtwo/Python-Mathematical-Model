# -*- coding:utf-8 -*-

# 蒙卡洛法求解非线性整数规划
import numpy as np
import time

start = time.time()
x = None
max_val = 0
number = 0
restrict_array = np.array([
    [1, 1, 1, 1, 1],
    [1, 2, 2, 1, 6],
    [2, 1, 6, 0, 0],
    [0, 0, 1, 1, 5]
])
sample_size = 10 ** 6
restrict_result = np.array([400, 800, 200, 200]).T
while number < sample_size:
    x = np.array([np.random.randint(100, size=5)])
    # 使用 dot 相乘而不是直接乘, 直接乘会有广播报错
    if (np.dot(restrict_array, x.T) <= restrict_result).all():
        # target = x_1^2 + x_2^2 + 3x_3^2 + 4x_4^2 + 2x_5^2 - 8x_1 - 2x_2 - 3x_3 - x_4 - 2x_5
        target = x[0, 0] ** 2 + x[0, 1] ** 2 + 3 * x[0, 2] ** 2 + 4 * x[0, 3] ** 2 + 2 * x[0, 4] ** 2
        target += -8 * x[0, 0] - 2 * x[0, 1] - 3 * x[0, 2] - x[0, 3] - 2 * x[0, 4]
        if target > max_val:
            max_val = target
    number += 1

end = time.time()
print("最大解:", max_val)
print("解集:", x)
print("计算用时", end - start)

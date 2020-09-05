# -*- coding:utf-8 -*-

import numpy as np
from scipy.optimize import linear_sum_assignment

# 求解指派问题

efficiency_array = np.array([
    [3, 8, 2, 10, 3],
    [8, 7, 2, 9, 7],
    [6, 4, 2, 7, 5],
    [8, 4, 2, 3, 5],
    [9, 10, 6, 9, 10]
])

row_index, column_index = linear_sum_assignment(efficiency_array)
print("安排数组:")
print(row_index+1)
print(column_index+1)
print("花费")
print(efficiency_array[row_index, column_index])
print("最小花费:", end="")
print(efficiency_array[row_index, column_index].sum())
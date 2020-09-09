# -*- coding:utf-8 -*-
import numpy as np
from scipy import optimize
from math import floor, ceil
import sys

epsilon = 1E-6


# 计算机求解整数线性规划往往会有很小的误差，如果使用传统的判断整数方法往往不好用
def is_integer(x):
    return abs(x - ceil(x)) < epsilon or abs(x - floor(x)) < epsilon


# 传统的比大小在这个时候也不好用了
# 自己定义一个小于函数
def lt(x, y):
    # 当 x y很接近的时候认为不存在小于关系
    if abs(x - y) < epsilon:
        return False
    else:
        return x < y


def gt(x, y):
    if abs(x - y) < epsilon:
        return False
    else:
        return x > y


def validate(x_seq) -> bool:
    for i in x_seq:
        # 判断是否为整数
        if not is_integer(i):
            return False
    return True


def get_first_non_int(x_seq):
    for i in range(len(x_seq)):
        if not is_integer(x_seq[i]):
            return i
    return None


class BranchBoundAlgorithm:

    def __init__(self, c, A, b, Aeq, beq, boundary, solution_max=None):
        self.c = c
        self.A = A
        self.b = b
        self.Aeq = Aeq
        self.beq = beq
        self.boundary = boundary
        self.solution_min = sys.maxsize
        self.global_best = None  # 全局最优解的范围

    def solve(self):
        res = optimize.linprog(self.c, self.A, self.b, self.Aeq, self.beq, bounds=self.boundary)
        x_seq = res.x
        if validate(x_seq):
            self.global_best = res
            self.solution_min = res.fun
            # 合法解
            return res.x, res.fun
        else:
            x_index = get_first_non_int(x_seq)
            if x_index is not None:
                x1_gt = ceil(x_seq[x_index])  # x <= [x] + 1
                x1_lt = floor(x_seq[x_index])  # x >= [x]
                # 设置新的边界大小
                temp = list(self.boundary)
                left_edge = temp[x_index][0]
                right_edge = temp[x_index][1]
                temp[x_index] = (left_edge, x1_lt)
                temp2 = temp.copy()
                temp2[x_index] = (x1_gt, right_edge)
                self._clc(temp, temp2)
                # 无解情况的考虑
                if not validate(self.global_best.x):
                    print("None Solution")
                    return None
                return self.global_best.x, self.solution_min
            else:
                print("ERROR")
                return res.x, res.fun

    def _clc(self, branch_bound1, branch_bound2):
        res1 = optimize.linprog(self.c, self.A, self.b, self.Aeq, self.beq, bounds=branch_bound1)
        res2 = optimize.linprog(self.c, self.A, self.b, self.Aeq, self.beq, bounds=branch_bound2)
        if not res1.success or gt(res1.fun, self.solution_min):
            # 无线性规划解或者当前最优解比最小值小，剪枝
            pass
        else:
            if validate(res1.x):
                # 是局部最优解
                self.solution_min = res1.fun
                self.global_best = res1
            else:
                # 分支
                x_index = get_first_non_int(res1.x)
                x_lt = floor(res1.x[x_index])
                x_gt = x_lt + 1
                temp = list(branch_bound1)
                left_edge = temp[x_index][0]
                right_edge = temp[x_index][1]

                if (left_edge > x_lt):
                    pass
                else:
                    temp[x_index] = (left_edge, x_lt)
                    temp2 = temp.copy()
                    if (right_edge is not None and x_gt > right_edge):
                        pass
                    else:
                        temp2[x_index] = (x_gt, right_edge)
                        self._clc(temp, temp2)

        if not res2.success or gt(res2.fun, self.solution_min):
            pass
        else:
            if validate(res2.x):
                self.solution_min = res2.fun
                self.global_best = res2
            else:
                x_index = get_first_non_int(res2.x)
                x_lt = floor(res2.x[x_index])
                x_gt = x_lt + 1
                temp = list(branch_bound2)
                left_edge = temp[x_index][0]
                right_edge = temp[x_index][1]
                if (left_edge > x_lt):
                    pass
                else:
                    temp[x_index] = (left_edge, x_lt)
                    temp2 = temp.copy()
                    if (right_edge is not None and x_gt > right_edge):
                        pass
                    else:
                        temp2[x_index] = (x_gt, right_edge)
                        self._clc(temp, temp2)


if __name__ == "__main__":
    c = np.array([-1, -1, -2])
    A = np.array([[7, 2, 3], [5, 4, 7], [2, 3, 5]])
    b = np.array([36, 42, 28])
    Aeq = None
    beq = None
    boundary = ((0, None), (0, None), (0, None))
    print(BranchBoundAlgorithm(c, A, b, Aeq, beq, boundary=boundary, solution_max=-4).solve())

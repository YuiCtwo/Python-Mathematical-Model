# -*- coding:utf-8 -*-
import numpy as np
from scipy import optimize
from math import floor, ceil
import sys

minsize = 1.0E-12


def validate(x_seq) -> bool:
    for i in x_seq:
        # 判断是否为整数
        if not i.is_integer():
            return False
    return True


def get_first_non_int(x_seq):
    for i in range(len(x_seq)):
        if int(x_seq[i]) != x_seq[i]:
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
        if solution_max is not None:
            self.solution_max = solution_max
        else:
            self.solution_max = 0
        self.solution_min = -sys.maxsize
        self.global_best = None  # 全局最优解的范围

    def solve(self):
        res = optimize.linprog(self.c, self.A, self.b, self.Aeq, self.beq, bounds=self.boundary)
        x_seq = res.x
        if validate(x_seq):
            # 合法解
            return res.x, res.fun
        else:
            x_index = get_first_non_int(x_seq)
            if x_index is not None:
                x1_lt = floor(x_seq[x_index])
                x1_gt = x1_lt + 1
                # 设置新的边界大小
                temp = list(self.boundary)
                left_edge = temp[x_index][0]
                right_edge = temp[x_index][1]
                self.global_best = res
                self.solution_min = res.fun
                temp[x_index] = (left_edge, x1_lt)
                temp2 = temp.copy()
                temp2[x_index] = (x1_gt, right_edge)
                self._clc(temp, temp2)
                return self.global_best.x, self.global_best.fun
            else:
                print("ERROR")
                return res.x, res.fun

    # TODO: 加入无解情况的考虑
    def _clc(self, branch_bound1, branch_bound2):
        res1 = optimize.linprog(self.c, self.A, self.b, self.Aeq, self.beq, bounds=branch_bound1)
        res2 = optimize.linprog(self.c, self.A, self.b, self.Aeq, self.beq, bounds=branch_bound2)
        validate1 = validate(res1.x)
        validate2 = validate(res2.x)
        cut1 = False
        cut2 = False
        # 找到最小
        if res1.fun < res2.fun:
            local_min = res1
        else:
            local_min = res2
        # 找出最小值作为新的最小值
        self.solution_min = min(self.solution_min, local_min.fun)
        # 找出符合解的最大值作为新的最大值
        if validate1:
            self.solution_max = min(self.solution_min, res1.fun)
        if validate2:
            self.solution_max = min(self.solution_min, res2.fun)

        # 解的最大值大于最优整数目标解最大值
        if res1.fun > self.solution_max:
            # 剪去
            cut1 = True
        if res2.fun > self.solution_max:
            # 剪去
            cut2 = True

        # 先判断剪不剪然后再分支
        if cut1:
            pass
        else:
            # 小于等于且满足整数条件
            if validate(res1.x):
                self.global_best = res1
            else:
                # 再次分支
                x_index = get_first_non_int(res1.x)
                x_lt = floor(res1.x[x_index])
                x_gt = x_lt + 1
                temp = list(self.boundary)
                left_edge = temp[x_index][0]
                right_edge = temp[x_index][1]
                temp[x_index] = (left_edge, x_lt)
                temp2 = temp.copy()
                temp2[x_index] = (x_gt, right_edge)
                self._clc(temp, temp2)

        if cut2:
            pass
        else:
            if validate(res2.x):
                self.global_best = res2
            else:
                x_index = get_first_non_int(res2.x)
                x_lt = floor(res2.x[x_index])
                x_gt = x_lt + 1
                temp = list(self.boundary)
                left_edge = temp[x_index][0]
                right_edge = temp[x_index][1]
                temp[x_index] = (left_edge, x_lt)
                temp2 = temp.copy()
                temp2[x_index] = (x_gt, right_edge)
                self._clc(temp, temp2)


if __name__ == "__main__":
    c = np.array([-1, -1, -2])
    A = np.array([[7, 2, 3], [5, 4, 7], [2, 3, 5]])
    b = np.array([36, 42, 28])
    Aeq = np.array([[0, 0, 0]])
    beq = np.array([0])
    boundary = ((0, None), (0, None), (0, None))
    print(BranchBoundAlgorithm(c, A, b, Aeq, beq, boundary=boundary, solution_max=-4).solve())

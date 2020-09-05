# 非参数 Bootstrap方法
# 没有标准库支持，尝试自己写一个类来通用解决问题
import random
import math
import numpy as np


class NonVarBoostrap:

    def __init__(self, data: list, capacity: int):
        self.data = data
        self.capacity = capacity

    def error_estimate(self, f, estimate, B=1000):
        # 误差估计
        result_list = []
        for i in range(0, B):
            # 随机进行容器大小的次数的抽样(有放回)
            sample_seq = random.choices(self.data, k=self.capacity)
            sample_data = f(sample_seq)
            result_list.append(sample_data)
        s = 0
        for i in result_list:
            s += (i - estimate) ** 2
        delta = math.sqrt(s / B)
        return delta

    def section_estimate(self, B, c, f):
        """
        求未知参数的 Bootstrap置信区间方法
        :param B: 抽样次数 通常 B>=1000
        :param c: 置信水平
        :param f: 样本估计量计算函数
        :return: bootstrap置信区间上下限
        """
        array = np.array(self.data)
        n = self.capacity
        sample_result_arr = []
        for i in range(B):
            # 获取随机的一组随机抽样数据
            index_arr = np.random.randint(0, n, size=n)
            data_sample = array[index_arr]
            sample_result = f(data_sample)
            sample_result_arr.append(sample_result)

        alpha = 1 - c
        k1 = int(B * alpha / 2)
        k2 = int(B * (1 - alpha / 2))
        auc_sample_arr_sorted = sorted(sample_result_arr)
        lower = auc_sample_arr_sorted[k1]
        higher = auc_sample_arr_sorted[k2]

        return lower, higher


# 给出样本，以样本的中位数作为整体中位数的估计，求该估计的标准误差的 Bootstrap 估计
def func(seq: list):
    return sum(seq) / len(seq)


# a = [18.2, 9.5, 12.0, 21.1, 10.2]
# b = NonVarBoostrap(data=a, capacity=5)
# print(b.error_estimate(f=func, estimate=func(a), B=1000))

a2 = [9, 8, 10, 12, 11, 12, 7, 9, 11, 8, 9, 7, 7, 8, 9, 7,
      9, 9, 10, 9, 9, 9, 12, 10, 10, 9, 13, 11, 13, 9]
b2 = NonVarBoostrap(data=a2, capacity=30)
print(b2.section_estimate(f=func, B=10000, c=0.9))

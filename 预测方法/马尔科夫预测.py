# 马尔科夫链，马尔科夫预测模型

import numpy as np
from copy import deepcopy


class MarkovChain:

    def __init__(self, distribution, states, scale):
        """
        @param
        @distribution: 初始状态概率
        @states: 状态转移矩阵
        @scale: 数据规模, scale=len(distribution)
        """
        self.distribution = np.array(distribution)
        self.states = np.array(states)
        self.scale = scale

    def activity_forecast(self, turn: int):
        # 指定次数状态转移后的分布概率
        result = self.distribution
        for i in range(turn):
            result = np.dot(result, self.states)
        return result

    def limiting(self):
        # 极限分布概率
        # 稳态概率时(π1π2π3……πn) = (π1π2π3……πn)P，P为状态转移矩阵
        # 如果 P-E矩阵的秩小于n，则存在稳态概率
        p = self.states.T - np.identity(self.scale)  # 记得转置
        if np.linalg.matrix_rank(p) < self.scale:
            print("Without limiting")
            return None
        n = deepcopy(self.states)
        n_next = np.dot(self.states, self.states)
        while not (n_next == n).all():
            n = n_next
            n_next = np.dot(n_next, self.states)
        return n


"""
例子参考课本 P431 页例 15.8
某计算机机房的一台计算机经常出故障，研究者每隔 15min 观察一次计算机的状态，共收集了 24 小时的数据，用1表示正常，0表示不正常
所得的数据序列为如下
"""

checkpoints = "1110010011111110011110111111001111111110001101101" \
            + "111011011010111101110111101111110011011111100111"

# 二维的一定没有极限的......
zero_to_zero = 8
zero_to_one = 18
one_to_zero = 18
one_to_one = 52
transforms = [
    [4/13, 9/13],
    [18/70, 52/70],
]
start = [26/97, 71/97]  # 初始状态的概率矩阵 [为 0, 为 1]
zero_one_chain = MarkovChain(start, transforms, 2)
print(zero_one_chain.activity_forecast(5))
print(zero_one_chain.limiting())
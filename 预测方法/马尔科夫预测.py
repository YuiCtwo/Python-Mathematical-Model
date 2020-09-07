# 马尔科夫链，马尔科夫预测模型

import numpy as np


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
        # 解多元一次方程的系数矩阵
        coff = self.states.T - np.identity(self.scale)
        result = np.zeros(self.scale).reshape(-1, 1)
        xs = np.linalg.solve(coff, result)
        return xs
# -*- coding:utf-8 -*-

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import time
plt.rcParams["font.sans-serif"] = ['SimHei']  # 显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
# 求 max f (0.05, 0.27, 0.19, 0.185, 0.185)*(x0, x1, x2, x3, x4).T
# 先转换为求解最小值，即所有系数前面加个负号就行了
# 从 a = 0 开始以步长为 0.001 循环搜索
# fig, ax = plt.subplots()
a = 0
a_seq = []
max_seq = []
while a < 0.05:
    c = np.array([-0.05, -0.27, -0.19, -0.185, -0.185])
    # 左右合并
    A = np.hstack((np.zeros((4, 1)), np.diag([0.025, 0.015, 0.055, 0.026])))
    b = a * np.ones((4, 1))
    # 注意这里必须让Aeq是一个5x1的 ndarray, 不然无法计算
    Aeq = np.array([[1, 1.01, 1.02, 1.045, 1.065]])
    beq = 1
    LB = np.zeros((5, 1))
    edge = ((0, None), (0, None), (0, None), (0, None), (0, None))
    # x>=0 表述为 bounds=(0, None)
    result = optimize.linprog(c, A, b, Aeq, beq, bounds=edge)
    # 最优解
    print(result.x)
    # 最小值
    print(result.fun)
    # 绘图
    a_seq.append(a)
    max_seq.append(-result.fun)
    a += 0.001


plt.plot(a_seq, max_seq, "r*-")
# 画出来点太密了, 效果不好
# for x, y in zip(a_seq, max_seq):
#     plt.text(x, y+0.01, '(%.3f, %.2f)' % (x, y), ha='center', va='bottom')

plt.title("风险度与最大收益关系")
plt.ylabel('Q')
plt.xlabel('a')
plt.xticks(np.linspace(0, 0.05, num=10))
plt.yticks(np.linspace(0, 0.5, num=10))
plt.savefig("fig"+str(int(time.time()))+".jpg")
plt.show()
# -*- coding:utf-8 -*-
import numpy as np
import math

RI_dict = {
    1: 0,
    2: 0,
    3: 0.58,
    4: 0.9,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.41,
    9: 1.45
}

principle_layer = [
    [1, 1, 1, 4, 1, 1/2],
    [1, 1, 2, 4, 1, 1/2],
    [1, 1/2, 1, 5, 3, 1/2],
    [1/4, 1/4, 1/5, 1, 1/3, 1/3],
    [1, 1, 1/3, 3, 1, 1],
    [2, 2, 2, 3, 3, 1]
]

method_layer = {
    "B1": [
        [1,  1/4, 1/2],
        [4,  1,     3],
        [2,  1/3,   1]
    ],
    "B2": [
        [1,  1/4, 1/5],
        [4,  1,   1/2],
        [5,  2,     1]
    ],
    "B3": [
        [1,   3,  1/3],
        [1/3, 1,  1/7],
        [3,   7,    1]
    ],
    "B4": [
        [1,   1/3,  5],
        [3,   1,    7],
        [1/5, 1/7,  1]
    ],
    "B5": [
        [1,   1,   7],
        [1,   1,   7],
        [1/7, 1/7, 1]
    ],
    "B6": [
        [1,    7,  9],
        [1/7,  1,  1],
        [1/9,  1,  1]
    ]
}

# 检验成对比较矩阵的一致性
principle_layer = np.array(principle_layer)
n = principle_layer.shape[0]
RI = RI_dict[n]
# 两个返回值，一个是特征值，另一个是特征向量
lambda_array, v = np.linalg.eig(principle_layer)
# 求 ndarray 最大的元素不能使用一般的 max 函数
lambda_max_index = np.argmax(lambda_array)
lambda_max = lambda_array[lambda_max_index]
CI = (lambda_max - n) / (n - 1)
CR = CI / RI
if CR < 0.1:
    print("矩阵一致性可接受")
    # 计算指标权重
    # 取最大特征值的特征向量然后归一化
    w = v[:, lambda_max_index]
    # 错误的获取方式 p = v[lambda_max_index]
    normalize_vectors = w / np.sum(w)
    print(normalize_vectors)
    single_layer_weights = []
    for key in method_layer:
        # 这里和上面的一起抽出一个函数最好
        w = np.array(method_layer[key])
        non_normalized_array = []
        for i in range(w.shape[0]):
            temp = 0
            for j in range(w.shape[0]):
                temp += w[i, j]
            non_normalized_array.append(temp)
        w = np.array(non_normalized_array)
        single_layer_weights.append((w / np.sum(w)).tolist())
    print(single_layer_weights)
    single_layer_weights = np.array(single_layer_weights)
    choices = np.dot(normalize_vectors, single_layer_weights)
    print("方案总权重:使用求和方法计算权向量", choices)
    print("最大值:", np.max(choices))

    single_layer_weights = []
    for key in method_layer:
        w = np.array(method_layer[key])
        lambda_array, v = np.linalg.eig(w)
        lambda_max_index = np.argmax(lambda_array)
        t = v[:, lambda_max_index]
        single_layer_weights.append((t / np.sum(t)).tolist())
    print(single_layer_weights)
    single_layer_weights = np.array(single_layer_weights)
    choices = np.dot(normalize_vectors, single_layer_weights)
    print("方案总权重:使用最大特征向量计算权向量", choices)
    print("最大值:", np.max(choices))
else:
    print("请做适当的修正")

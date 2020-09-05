# -*- coding:utf-8 -*-
import sys
INFINITE = sys.maxsize
graphic = [
    [0,        2,        6,        4],
    [INFINITE, 0,        3,        INFINITE],
    [7,        INFINITE, 0,        1],
    [5,        INFINITE, 12,       0]
]


def floyd(graph_matrix):
    n = len(graph_matrix)
    # 构造 path 数组
    path = []
    for i in range(n):
        path.append([])
    # 初始化
    for i in range(n):
        for j in range(n):
            path[i].append(j)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph_matrix[i][k] == sys.maxsize or graph_matrix[k][j] == sys.maxsize:
                    continue
                temp = graph_matrix[i][k] + graph_matrix[k][j]
                if temp < graph_matrix[i][j]:
                    graph_matrix[i][j] = temp
                    # 更新路径
                    path[i][j] = path[i][k]
    return graph_matrix, path


def print_path(path_matrix):
    n = len(path_matrix)
    for i in range(n):
        for j in range(n):
            print("{}->{}:".format(i, j), end="")
            print("{}->".format(i), end="")
            temp = path_matrix[i][j]
            while True:
                # 存在中转的情况, 以中转为起点
                temp = path_matrix[temp][j]
                if temp == j:
                    print(j)
                    break
                else:
                    print("{}->".format(temp), end="")


graph, path = floyd(graphic)
print(path)
print(graph)
print_path(path)



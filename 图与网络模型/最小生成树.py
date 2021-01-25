# -*- coding:utf-8 -*-
import sys

# Prim法构造最小生成树

maximum = sys.maxsize
graph = [
    [0, 50, 60, maximum, maximum, maximum, maximum],
    [50, 0, maximum, 65, 40, maximum, maximum],
    [60, maximum, 0, 52, maximum, maximum, 45],
    [maximum, 65, 52, 0, 50, 30, 42],
    [maximum, 40, maximum, 50, 0, 70, maximum],
    [maximum, maximum, maximum, 30, 70, 0, maximum],
    [maximum, maximum, 45, 42, maximum, maximum]
]

candidate_node = [1, 2, 3, 4, 5, 6, 7]


# Prim算法求最小生成树
def prim():
    start = 1
    selected_node = [start]
    candidate_node.remove(start)
    length = len(candidate_node)
    while length != 0:
        end_node = candidate_node[0]
        # 找到距离被选中结点中有最小边的点
        for start_node in selected_node:
            for node in candidate_node:
                if graph[start_node-1][end_node-1] > graph[start_node-1][node-1]:
                    end_node = node
        # 删去选择的顶点
        selected_node.append(end_node)
        candidate_node.remove(end_node)
        length = length - 1

    return selected_node


# Kruskal 算法求最小生成树
# 邻接表存数据
adjacency_lists = [
    [(2, 50), (3, 60)],
    [(4, 65), (5, 40)],
    [(4, 52), (7, 45)],
    [(5, 50), (6, 30)],
    [(6, 70)]
]


def kruskal(node_num:int):
    edges = []
    # 初始化
    selected_edges = []
    # 处理数据使我们的后续操作更容易
    for i in range(len(adjacency_lists)):
        for unit in adjacency_lists[i]:
            edges.append((i+1, unit[0], unit[1]))
    # 排序
    edges.sort(key=lambda x: x[2])
    group = [[i] for i in range(node_num)]
    for edge in edges:
        m = n = 0
        for i in range(len(group)):
            if edge[0] in group[i]:
                m = i
            if edge[1] in group[i]:
                n = i
        if m != n:
            selected_edges.append(edge)
            # 被选中的线的终点加入起点所在的列表
            # 被选中的线的终点的列表被清空
            # group[i] 表示联通的点的集合
            group[m] = group[m] + group[n]  # 列表合并
            group[n] = []

    return selected_edges

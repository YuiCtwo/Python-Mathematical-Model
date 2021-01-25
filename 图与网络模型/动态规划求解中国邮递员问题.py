# -*- coding:utf-8 -*-
import sys


# 方法 1 使用动态规划来搜索最小组合
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


def shortest_path(graph_matrix, d):
    """
    :param graph_matrix: 邻接矩阵
    :param d: 度数组
    :return: 最短路径
    """
    # 度为奇数的顶点
    graph_matrix, _ = floyd(graph_matrix)
    odd_points = [0]  # 初始化包含0便于后续dp数组dp[0]的计算
    for i, di in enumerate(d):
        if di % 2 == 1:
            odd_points.append(i)
    # 奇度顶点的个数
    odd_num = len(odd_points) - 1
    dp = [0]  # dp[0] 无一个点所以长度也为0
    dp_length = 1 << odd_num
    # 初始化数组填入最大的数
    for i in range(dp_length):
        dp.append(sys.maxsize)
    for i in range(dp_length):
        x = 1
        while (1 << (x - 1)) & i:
            # 选择不在当前集合的点x
            x += 1
        for y in range(x + 1, odd_num + 1):  # x+1 <= y <= odd_num
            # 选择不在集合内的与x不同的y
            if (1 << (y - 1)) & i:
                continue
            else:
                # 计算
                binary_pt = i | (1 << (x - 1)) | (1 << (y - 1))  # 新形成的集合
                if graph_matrix[odd_points[x]][odd_points[y]] == sys.maxsize:
                    # x,y 不连通
                    pass
                elif dp[i] == sys.maxsize:
                    # 对于这个组合无最短路径
                    pass
                else:
                    trail = dp[i] + graph_matrix[odd_points[x]][odd_points[y]]
                    # 更新最短路径
                    dp[binary_pt] = min(dp[binary_pt], trail)
    # print(dp[dp_length-1])
    return dp[dp_length - 1]


def main():
    # 记录的所有路求和
    n = 0
    d = []
    min_length = 0
    with open("中国邮递员问题测试数据1.txt", 'r') as fp:
        scales = fp.readline()
        n, m = map(int, scales.split(' '))
        # 初始化
        for i in range(n):
            d.append(0)
        graph = [[sys.maxsize] * n for _ in range(n)]
        # 读入数据
        for line in fp.readlines():
            start_point, end_point, weight = map(int, line.split(' '))
            # 点标号从 1 开始
            start_point -= 1
            end_point -= 1
            d[start_point] += 1
            d[end_point] += 1
            # 无向图
            graph[start_point][end_point] = weight
            graph[end_point][start_point] = weight
            min_length += weight
    print(graph)
    print("最小路径长度为:", end='')
    t = 0
    for di in d:
        if di % 2 == 0:
            t += 1
    if t == n:
        # 所有点读数都是偶数度，为欧拉图
        pass
    else:
        min_length += shortest_path(graph, d)
    print(min_length)


if __name__ == '__main__':
    main()

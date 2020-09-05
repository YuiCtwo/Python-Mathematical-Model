import sys
import numpy as np
MAX = sys.maxsize
# dijkstra 算法
# 个人的实现

graph = [
    [0, MAX, 10, MAX, 30, 100],
    [MAX, 0, 5, MAX, MAX, MAX],
    [MAX, MAX, 0, 50, MAX, MAX],
    [MAX, MAX, MAX, 0, MAX, 10],
    [MAX, MAX, MAX, 20, 0, 60],
    [MAX, MAX, MAX, MAX, MAX, 0]
]


# 以 0 为起始点
def dijkstra(route_matrix):
    # 节点数
    point_num = len(graph)
    # 初始化路径数组
    dis = [0] * point_num
    # 初始化点集
    path = [0] * point_num
    for i in range(0, point_num):
        dis[i] = graph[0][i]
        if dis[i] == MAX:
            path[i] = -1
    # 选中的点
    selected_point = [0]
    # 上一个选中的点
    last_selected_point = 0

    length = len(selected_point)
    while length != point_num:
        # 选出路径中的最小值
        min_route = MAX
        flag = -1
        for i in range(0, point_num):
            if i in selected_point:
                pass
            else:
                if dis[i] <= min_route:
                    flag = i
                    min_route = dis[i]
        # 加入路径点
        selected_point.append(flag)

        # 最小值为无穷，即计算到 v0无法到达的点，退出循环
        if dis[flag] == MAX:
            break

        # 计算加上加入的点到达其他点的距离
        # 刷新最小路径
        for point in range(0, point_num):
            # 不再计算已经选中的点
            if point in selected_point:
                pass
            else:
                # 防止计算加法溢出
                if route_matrix[flag][point] == MAX:
                    pass
                else:
                    route_lens = route_matrix[flag][point] + dis[flag]  # 加入的点到其余点的距离 + 原点到加入的点的距离
                    # 用小值替换掉 dis 数组中的值
                    if route_lens < dis[point]:
                        dis[point] = route_lens
                        # 最短路径 flag 点 -> 上一个选中的点
                        path[flag] = last_selected_point
        last_selected_point = flag
        length = len(selected_point)
    return path, dis


_, dis = dijkstra(graph)
print(dis)
print(_)
# 库函数


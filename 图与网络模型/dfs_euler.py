# -*- coding:utf-8 -*-

route = []


def euler(index: int, edge):
    if index in edge:
        n = len(edge[index])
    else:
        n = 0
    for i in range(0, n):
        temp = edge[index][i]
        # 没有路
        if temp == -1:
            continue
        else:
            # 路走过之后不再走
            # print(index)
            # t = edge[index][i]
            edge[index][i] = -1
            # d = edge[t].index(index)
            # edge[t][d] = -1
            # 从 temp 点开始的 euler 回路
            euler(temp, edge)
            route.append((temp, index))


if __name__ == "__main__":
    adjacency_list = {}
    with open("欧拉回路测试数据.txt", 'r') as fp:
        scales = fp.readline()
        n, m = map(int, scales.split(' '))
        for line in fp.readlines():
            start_point, end_point = map(int, line.split(' '))
            # 输入的点标号从 1 开始
            start_point -= 1
            end_point -= 1
            # 构造邻接表
            if start_point in adjacency_list.keys():
                adjacency_list[start_point].append(end_point)
            else:
                adjacency_list[start_point] = [end_point]
            # if end_point in adjacency_list.keys():
            #     adjacency_list[end_point].append(start_point)
            # else:
            #     adjacency_list[end_point] = [start_point]
    print(adjacency_list)
    euler(0, adjacency_list)
    print(route)
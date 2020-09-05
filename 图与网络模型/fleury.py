# -*- coding:utf-8 -*-


class Fleury:

    def __init__(self, graph):
        self.graph = graph
        self.start = -1
        self.route = []
        self.num = len(graph)  # 图中的点数

    def solve(self, current, start):
        flag = False  # 是否还有与x关联的边
        # 倒回会导致上一个点被多记录一次
        if self.route and self.route[-1] == current:
            pass
        else:
            self.route.append(current)
        for i in range(start, self.num):
            # 从 start 开始搜索是否有边
            if self.graph[i][current] > 0:
                # i 与 current 有边
                flag = True
                # 删除边
                self.graph[i][current] -= 1
                self.graph[current][i] -= 1
                self.solve(i, 0)  # 从 i 开始搜索
                break
        if not flag:
            # 如果没有边与当前节点 current 相连
            print(self.route)
            self.route.pop()
            # if len(self.route) == self.num:
            #     return self.route
            if self.all_zeros():
                self.route.append(start)
                return self.route
            else:
                # 回溯
                temp = self.route[-1]
                # 恢复上一次的 2 条边
                self.graph[temp][current] += 1
                self.graph[current][temp] += 1
                new_start = current + 1
                # 路径包含所有的点
                self.solve(temp, new_start)

    def all_zeros(self):
        for i in range(0, self.num):
            for j in range(0, self.num):
                if self.graph[i][j] != 0:
                    return False
        return True


if __name__ == "__main__":
    with open("欧拉回路测试数据.txt", 'r') as fp:
        scales = fp.readline()
        n, m = map(int, scales.split(' '))
        adjacency_list = [[0] * n for _ in range(n)]
        for line in fp.readlines():
            start_point, end_point = map(int, line.split(' '))
            # 输入的点标号从 1 开始
            start_point -= 1
            end_point -= 1
            # 构造特殊的邻接矩阵
            adjacency_list[start_point][end_point] += 1
            adjacency_list[end_point][start_point] += 1
            # if end_point in adjacency_list.keys():
            #     adjacency_list[end_point].append(start_point)
            # else:
            #     adjacency_list[end_point] = [start_point]
    print(adjacency_list)
    f = Fleury(adjacency_list)
    f.solve(0, 0)
    print(f.route)


# -*- coding:utf-8 -*-
# km 最大流算法
import sys
from fleury import Fleury


def euler(index, edge):
    f = Fleury(edge)
    f.solve(index, index)
    return f.route



def floyd(graph_matrix):
    n = len(graph_matrix)
    # 构造 path 数组
    # 如果没有清 0 我们需要手动清0
    for i in range(n):
        graph_matrix[i][i] = 0
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

    for i in range(n):
        graph_matrix[i][i] = sys.maxsize

    return graph_matrix, path


class KM:
    lx = {}  # 一边的标号
    ly = {}  # 另一边的标号
    visit_x = {}  # 该点在增广路匹配过程中是否被尝试过
    visit_y = {}
    match = {}  # 匹配的映射关系
    slack = {}  # slack 优化

    def __init__(self, graph: dict):
        self.graph = graph
        # 初始化均未被访问
        for p in graph.keys():
            self.visit_x[p] = False
            self.lx[p] = -1
            self.visit_y[p] = False
            self.ly[p] = -1
            self.match[p] = -1
        print(self.visit_x, self.visit_y)

    def _extended_path(self, x):
        # 寻找增广路径
        # x 点被选择
        print(self.match)
        self.visit_x[x] = True
        for y in self.visit_y.keys():
            if self.visit_y[y]:
                # 结点被访问过了
                continue
            if self.graph[x][y] == sys.maxsize:
                # 不连通
                continue
            temp = self.lx[x] + self.ly[y] - self.graph[x][y]
            if temp == 0:
                # x, y 在相等子图中
                self.visit_y[y] = True
                if self.match[y] == -1 or self._extended_path(self.match[y]):
                    # 如果 y 元素没有对应的匹配或者 y 有新的匹配点
                    self.match[y] = x
                    return True
            elif self.slack[y] > temp:
                # slack 优化
                self.slack[y] = temp
            else:
                pass
        # 无增广路径
        return False

    def _solve(self):
        for x in self.visit_x:
            # 对所有的 x 寻找增广回路
            # 重新初始化 slack 中的数值
            for y in self.visit_y:
                self.slack[y] = sys.maxsize
            while True:
                # 求新的增广回路，重新初始化访问数组
                for y in self.visit_y:
                    self.visit_y[y] = False
                for xt in self.visit_x:
                    self.visit_x[xt] = False
                if self._extended_path(x):
                    # 有增广回路
                    break  # 跳出循环，判断下一个点
                else:
                    delta = sys.maxsize
                    # 求得需要对定标进行运算的 d
                    for y in self.visit_y:
                        # y 在交错树外，x 在交错树中（dfs失败x一定在交错树中）
                        if (not self.visit_y[y]) and delta > self.slack[y]:
                            delta = self.slack[y]
                    # 对定标的值修正，下一步一定可以再加入一个点
                    for xt in self.visit_x:
                        if self.visit_x[xt]:
                            self.lx[xt] -= delta
                    for yt in self.visit_y:
                        if self.visit_y[yt]:
                            self.ly[yt] += delta
                        else:
                            # 修改顶标后，要把所有的slack值都减去delta
                            # 这是因为x点的标定值减小了delta
                            # 根据slack的计算也需要变换和x点相关的点的slack值
                            self.slack[yt] -= delta

    def km_solve(self, is_max=True):
        # 初始化
        if not is_max:
            for v_dict in self.graph.values():
                for pv in v_dict:
                    v_dict[pv] = -v_dict[pv]
        for x in self.lx:
            # 贪心算法, 初始化为点最大的权的边
            self.lx[x] = max(list(self.graph[x].values()))
            # 求最小值还是最大值
            # if is_max:
            #     pass
            # else:
            #     self.lx[x] = -self.lx[x]
        for y in self.ly:
            self.ly[y] = 0
        self._solve()
        part_match = {}
        temp_s = 0
        for k, v in self.match.items():
            temp_s += self.graph[k][v]
            if k in part_match.keys() or k in part_match.values():
                pass
            else:
                part_match[k] = v
        self.match = part_match
        print(part_match)
        print(temp_s)
        # 匹配整体计算了2次
        if is_max:
            return temp_s / 2
        else:
            return -temp_s / 2


d = []
min_length = 0
adjacency_array = []  # 邻接矩阵
with open("中国邮递员问题测试数据2.txt", 'r') as fp:
    scales = fp.readline()
    n, m = map(int, scales.split(' '))
    # 初始化
    for i in range(n):
        d.append(0)
    graph = [[sys.maxsize]*n for _ in range(n)]
    adjacency_array = [[0]*n for _ in range(n)]
    # 读入数据
    # 要求读入的数据要满足邻接表的排布
    for line in fp.readlines():
        start_point, end_point, weight = map(int, line.split(' '))
        # 输入的点标号从 1 开始
        start_point -= 1
        end_point -= 1
        # 构造邻接矩阵
        adjacency_array[start_point][end_point] += 1
        adjacency_array[end_point][start_point] += 1
        d[start_point] += 1
        d[end_point] += 1
        # 无向图
        graph[start_point][end_point] = weight
        graph[end_point][start_point] = weight
        min_length += weight
t = 0
for di in d:
        if di % 2 == 0:
            t += 1
if t == n:
    # 所有点读数都是偶数度，为欧拉图
    route = euler(0, adjacency_array)
else:
    odd_points = []  # 记录奇数度顶点的数组
    for i, di in enumerate(d):
        if di % 2 == 1:
            odd_points.append(i)
    # 奇度顶点的个数
    graph_matrix, path = floyd(graph)
    # 奇度顶点组成子图
    sub_graph = {}
    for odd_p in odd_points:
        sub_graph[odd_p] = {}
        for end_p in odd_points:
            sub_graph[odd_p][end_p] = graph_matrix[odd_p][end_p]
    km_solution = KM(sub_graph)
    # 求最小解
    min_length += km_solution.km_solve(False)
    # 删去匹配的边
    for k, v in km_solution.match.items():
        start = k
        temp = path[k][v]
        while True:
            # 存在中转的情况, 以中转为起点
            adjacency_array[start][temp] += 1
            adjacency_array[temp][start] += 1
            if temp == v:
                break
            else:
                pass
            start = temp
            temp = path[temp][v]

    route = euler(0, adjacency_array)
for p in route:
    print("({})".format(p+1), end='')
print("最小路径长度为:", end='')
print(min_length)
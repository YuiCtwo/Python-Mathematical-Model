
# 有向网采用邻接表的形式存储


# class ALGraph:
#     vex_num:int = 0  # 顶点数
#     arc_num:int = 0  # 弧数
#     adj_list:list = []  # (顶点, 距离)
#     p:int = 0
#     def next_vertex(self):
#         return self.adj_list[self.p]

def topological_order(adj_graph: list, adj_graph_r: list, num: int):
    """

    :param adj_graph: 邻接表矩阵, list 嵌套, 每个单元为一个三元组
    :param num: 结点个数
    :param adj_graph_r: 逆邻接表
    :return: None
    """
    ve = {}
    result = []
    earlier = []
    later = []
    for i in range(num):
        ve[i] = 0
        earlier.append(0)
    # 求入度
    for adj_list in adj_graph:
        for vertex in adj_list:
            ve[vertex[0]] += 1
    # 将入度为 0的点压栈
    stack = []
    for key in ve.keys():
        if ve[key] == 0:
            stack.append(key)
    while stack:
        # 栈顶元素加入拓扑序列中
        v = stack.pop()
        result.append(v)
        # 相关的点入度都减 1
        for vertex in adj_graph[v]:
            vertex_order = vertex[0]
            ve[vertex_order] -= 1
            # 如果为 0则入栈
            if ve[vertex_order] == 0:
                stack.append(vertex_order)
            # 求最早计划开始时间
            t = earlier[v] + vertex[1]
            if t > earlier[vertex_order]:
                earlier[vertex_order] = t
    # 求最早发生时间完成
    # ----------------
    # 求最迟开始时间
    for i in range(num):
        # 初始化最迟开始时间和最早开始时间一样
        later[i] = earlier[num-1]
    # 拓扑逆序求各顶点的最迟时间
    while result:
        j = result.pop()
        # j点的前驱
        for vertex in adj_graph_r[j]:
            for p in vertex:
                t = later[j] - p[1]
                if later[p[0]] > t:
                    later[p[0]] = t
    print("Critical Events:")
    for i in range(num):
        if later[i] == earlier[i]:
            print("event ", i)


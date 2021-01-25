# docplex其实是一个建模语言，然后调用 CPLEX引擎求解，此时python是作为建模语言
# 安装教程: https://zhuanlan.zhihu.com/p/54894350
# 官方文档: https://github.com/IBMDecisionOptimization/docplex-doc
from docplex.mp.model import Model

# 有点像 Lingo的写法
# model = Model()  # 创建模型
# var_list = [i for i in range(0, 3)]  # 创建参数列表
# X = model.binary_var_list(var_list, lb=0, name='X')  # 创建变量列表
#
# # 设定目标函数
# model.maximize(X[0] + X[1] + 2*X[2])
#
# # 添加约束条件
# model.add_constraint(7*X[0] + 2*X[1] + 3*X[2] <= 36)
# model.add_constraint(5*X[0] + 4*X[1] + 7*X[2] <= 42)
# model.add_constraint(2*X[0] + 3*X[1] + 5*X[2] <= 28)
# sol = model.solve()  # 求解模型
# print(sol)

# 有时求出来的不是最优解，参考上下两个不同的例子

model = Model()
var_list = [i for i in range(0, 7)]
X = model.binary_var_list(var_list, lb=0, name='X')
model.maximize(11 * X[0] + 9 * X[1] + 29 * X[2] + 9 * X[3] + 21 * X[4] + 31 * X[5] + 22 * X[6])
model.add_constraint(X[0] + X[1] + X[2] <= 2)
model.add_constraint(X[3] + X[4] >= 1)
model.add_constraint(X[5] + X[6] >= 1)
model.add_constraint(10 * X[0] + 8 * X[1] + 20 * X[2] + 5 * X[3] + 13 * X[4] + 22 * X[5] + 10 * X[6] <= 60)
sol = model.solve()
print(sol)

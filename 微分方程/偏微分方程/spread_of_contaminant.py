import numpy as np
import math
import matplotlib.pyplot as plt


def u0(x):
    # 高斯函数
    mean = 0.2
    sigma = 0.025
    return (1/160)*np.exp(-1 * ((x - mean) ** 2) / (2 * (sigma ** 2))) / (math.sqrt(2 * np.pi) * sigma)


# init_ux():
# xs = np.linspace(0, 1, 1000)
# ys = [u0(x) for x in xs]
# plt.plot(xs, ys, "b-")
# plt.ylabel(r"$u_0(x)$")
# plt.yticks([round(x, 2) for x in np.linspace(0, 0.1, 10)])
# plt.savefig("init_ux.png")
# plt.show()
sample_num = 5
nSpace = 600
nTime = 1000
xs = np.linspace(0, 1, nSpace-1)
k = 5e-4
c = -0.5
dt = 1/nTime
h = 1/nSpace
A = np.zeros((nSpace-1, nSpace-1))
u = np.zeros((nSpace-1, 1))

for i in range(nSpace-1):
    u[i][0] = u0(i*h)

for i in range(1, nSpace-1-1):
    A[i][i-1] = k / (h * h) - c / h
    A[i][i] = (-2 * k) / (h * h) + c / h
    A[i][i+1] = k / (h * h)
# 采用欧拉方法
times = 0
t = 0
u_record = [u.T.tolist()[0]]
while t <= 1:
    u = u + dt * A.dot(u)
    t += dt
    times += 1
    # 每 200 次迭代记录一次
    if times == nTime/sample_num:
        u_record.append(u.T.tolist()[0])
        times = 0


# 采用二阶龙格库塔法
u = np.zeros((nSpace-1, 1))
for i in range(nSpace-1):
    u[i][0] = u0(i*h)
t = 0
times = 0

while t <= 1:
    k1 = A.dot(u)
    k2 = A.dot(u+k1*dt)
    u = u + 0.5 * dt * (k1 + k2)
    t += dt
    times += 1
    if times == nTime/sample_num:
        u_record.append(u.T.tolist()[0])
        times = 0

# 绘图
print(len(u_record))
values_fe = [int(i*250/10) for i in range(10)]
values_rk2 = [int(i*250/10) for i in range(10)]
colors_fe = ["#%02x%02x%02x" % (120, int(g), 200)for g in values_fe]
colors_rk2 = ["#%02x%02x%02x" % (200, int(g), 40)for g in values_rk2]

for i in range(sample_num):
    if i == 0:
        plt.plot(xs, u_record[i], color="#000080", linewidth=2, label="Init u")
    elif i == 1:
        plt.plot(xs, u_record[i], color=colors_fe[i], linewidth=2, label="FE Method")
    else:
        plt.plot(xs, u_record[i], color=colors_fe[i], linewidth=2)
for i in range(sample_num):
    if i == 0:
        plt.plot(xs, u_record[sample_num + i], color=colors_rk2[i], linewidth=2, label="RK2 Method")
    else:
        plt.plot(xs, u_record[sample_num + i], color=colors_rk2[i], linewidth=2)

plt.title("Evolution of u")
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.legend(loc="best")
plt.savefig("ux.png")
plt.show()

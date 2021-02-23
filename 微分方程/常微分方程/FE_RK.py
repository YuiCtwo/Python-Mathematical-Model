import math
import matplotlib.pyplot as plt


coff = 10
u0 = 1
t_final = 1
fe_error = []
rk4_error = []


def f(t, u):
    return -coff * u


def true_f(u):
    return u0 * math.exp(-coff*u)


def forward_euler(f, u0, dt, t_final):
    t = 0
    u = u0
    while t < t_final:
        u = u + dt * f(t, u)
        t = t + dt
    return u


def rk4(f, u0, dt, t_final):
    t = 0
    u = u0
    while t < t_final:
        t_half = t + 0.5 * dt
        t_next = t + dt
        k1 = dt * f(t, u)
        u1 = u + 0.5 * k1
        k2 = dt * f(t_half, u1)
        u2 = u + 0.5 * k2
        k3 = dt * f(t_half, u2)
        u3 = u + k3
        k4 = dt * f(t_next, u3)
        u = u + (1/6) * (k1 + 2 * (k2 + k3) + k4)
        # 更新 t
        t = t_next
    return u


dt_vec = [1e-4, 2e-4, 1e-3, 2e-3, 1e-2, 2e-2, 1e-1]
for i in range(0, len(dt_vec)):
    dt = dt_vec[i]
    fe_result = forward_euler(f, u0, dt, t_final)
    rk_result = rk4(f, u0, dt, t_final)
    fe_error.append(abs(true_f(t_final) - fe_result))
    rk4_error.append(abs(true_f(t_final) - rk_result))

# 绘图
plt.loglog(dt_vec, fe_error, "r-", label="Forward Euler Error")
plt.loglog(dt_vec, rk4_error, "b", label="RK4 Error")
plt.xlabel("dt")
# y 轴设置反向
# ax = plt.gca()
# ax.invert_yaxis()

plt.ylabel("error")
plt.legend()
plt.savefig("fe_rk.png")
plt.show()
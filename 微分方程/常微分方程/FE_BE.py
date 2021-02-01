# 显式欧拉和隐式欧拉的对比
import math
import matplotlib.pyplot as plt
import numpy as np

llam = 100  # change there in 1 10 100
u0 = 3
t_final = 3 * math.pi
dt = 1e-1


def dudt(t, u):
    return -llam * (u - math.cos(t)) - math.sin(t)


def tf(t):
    return (u0 - 1) * math.exp(-llam * t) + math.cos(t)


def forward_euler(f, u0, dt, t_final):
    us = [u0]
    u = u0
    t = 0
    for i in range(0, int(t_final/dt)):
        u = u + dt * f(t, u)
        us.append(u)
        t += dt
    return us


def backward_euler(f, u0, dt, t_final, lam):

    # newton nonlinear solver function
    def newton(t, u, f, dt, lam):
        uu = u
        g = lambda x: ((x - u) / dt - f(t, x))
        j = lambda x: 1 / dt + lam
        for _ in range(1, 100):
            u_next = uu - g(uu) / j(uu)
            uu = u_next
            if abs(g(u_next)) <= 1e-14:
                break
        return uu

    us = [u0]
    u = u0
    t = 0
    for i in range(0, int(t_final/dt)):
        # 注意这里是 t_i+1
        u = newton(t+dt, u, f, dt, lam)
        us.append(u)
        t += dt
    return us


t_true = np.linspace(0, t_final, 1000)
u_true = [tf(t) for t in t_true]
plt.plot(t_true, u_true, 'b', label="True Function")
t = [i*dt for i in range(0, int(t_final/dt)+1)]
uFE = forward_euler(dudt, u0, dt, t_final)
uBE = backward_euler(dudt, u0, dt, t_final, llam)
err_FE = np.mean([abs(uFE[i] - u_true[i]) for i in range(len(uFE))])
err_BE = np.mean([abs(uBE[i] - u_true[i]) for i in range(len(uFE))])
print("Error of Forward Euler: ", err_FE)
print("Error of Backward Euler: ", err_BE)
plt.plot(t, uFE, "r-", label="Forward Euler")
plt.plot(t, uBE, "g-", label="Backward Euler")
plt.legend()
plt.savefig("./fe_be.png")
plt.show()

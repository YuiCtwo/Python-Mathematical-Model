# -*- coding:utf-8 -*-
import numpy as np
from scipy import linalg
xs = np.array([-1.00, -0.75, -0.50, -0.25, 0,
               0.25, 0.50, 0.75, 1.00])
ys = np.array([-0.2209, 0.3295, 0.8826, 1.4392, 2.0003,
               2.5645, 3.1334, 3.7061, 4.2836])
A = np.vstack([xs**0, xs**1])
sol, r, rank, s = linalg.lstsq(A.T, ys)
print("{} + {}x".format(sol[0], sol[1]))

A = np.vstack([xs**0, xs**1, xs**2])
sol, r, rank, s = linalg.lstsq(A.T, ys)
print("{} + {}x + {}x^2".format(sol[0], sol[1], sol[2]))


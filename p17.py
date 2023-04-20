#!/usr/bin/env python

import numpy as np
import numpy.linalg as lg

A_n = lambda n: np.array(object=[[1, 2], [2, 4 + 1 / np.square(n)]])
b_n = lambda n: np.array(object=[[1, 2 - 1 / np.square(n)]])
x_tilde = np.array([[1, 0]])
x_n = lambda n: lg.solve(a=A_n(n), b=b_n(n).T)
r_n = lambda n: A_n(n) @ x_n(n) - b_n(n)

kappa_n = lambda n: la.norm(x=A_n(n), ord=np.inf) * la.norm(
    x=la.inv(a=A_n(n)), ord=np.inf
)

for n in range(1, 100):
    print(f"x_{n}:\n{x_n(n)}")

#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

A = np.array(object=[[2, 3], [5, 4]])
b = np.array(object=[8.0, 16.4]).T
x = la.solve(a=A, b=b)
kappa = lambda A: la.norm(x=A, ord=np.inf) * la.norm(x=la.inv(a=A), ord=np.inf)
# print(A_inv @ b)

if __name__ == "__main__":
    print(f"A=\n{A}\nb=\n{b}\nx={x}\nA^{-1}=\n{la.inv(a=A)}\nk_A={kappa(A)}")

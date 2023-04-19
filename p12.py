#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

A = np.array(object=[[1, 2], [3, 4]])
kappa = la.norm(x=A, ord=np.inf) * la.norm(x=la.inv(a=A), ord=np.inf)

if __name__ == "__main__":
    print(kappa)

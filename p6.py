#!/usr/bin/env python


def I(N):
    """
    I(0)  = ln(6 / 5)
    I(k) = 1 / k - 5 * I(k - 1)
    """
    from math import log

    I = log(6 / 5)
    print(f"I({0}) = {I}")

    for k in range(1, N):
        I = 1 / k + 5 * I
        print(f"I({k}) = {I}")


def I_exact():
    from sympy import symbols, integrate

    n = symbols("n", integer=True, positive=True)
    x = symbols("x", real=True)

    print(integrate(x**n / (5 + x), (x, 0, 1)))


def table():
    from tabulate import tabulate
    import pandas as pd

    x = [1, 2, 3]
    y = [2, 4, 6]
    df = pd.DataFrame({"x": x, "y": y})
    df.index += 1
    print(tabulate(df, headers="keys", floatfmt=".12f"))


if __name__ == "__main__":
    # I(100)
    # I_exact()
    table()

#!/usr/bin/env python

# Convert integer decimal to binary


def idecimal2binary(number: int):
    temp: list = []
    while number >= 1:
        temp.insert(0, number % 2)
        number //= 2
    return "".join(str(i) for i in temp)


def fdecimal2binary(r: float):
    # Paso 0
    k = 1
    r_1 = r
    lista = list(["0", "."])
    # Paso 2
    if (2 * r_1) >= 1:
        d_k = 1
    else:
        d_k = 0

    counter = 0  # en caso sea infinito

    while True:
        r_1 = 2 * r_1 - d_k
        lista.append(d_k)
        if r_1 == 0:
            break
        else:
            k += 1
            if (2 * r_1) >= 1:
                d_k = 1
            else:
                d_k = 0
        if counter > 100:
            break

    return "".join(str(i) for i in lista)


if __name__ == "__main__":
    print(f"{10} = ({idecimal2binary(10)})_2")
    print(f"{0.25} = ({fdecimal2binary(0.25)})_2")
    print(f"{6} = ({idecimal2binary(6)})_2")
    print(f"{0.75} = ({fdecimal2binary(0.75)})_2")
    print(f"{17} = ({idecimal2binary(17)})_2")
    print(f"{0.00} = ({fdecimal2binary(0.00)})_2")
    print(f"{52} = ({idecimal2binary(52)})_2")
    print(f"{0.21875} = ({fdecimal2binary(0.21875)})_2")
    print(f"{130} = ({idecimal2binary(130)})_2")
    # print(f"{0.01001} = ({fdecimal2binary(0.01001)})_2")
    print(f"{129} = ({idecimal2binary(129)})_2")
    print(f"{131} = ({idecimal2binary(131)})_2")

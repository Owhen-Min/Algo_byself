def xnor(n1, n2):
    return (~(n1 ^ n2))& ((1 << 3) - 1)


print(xnor(2, 3))
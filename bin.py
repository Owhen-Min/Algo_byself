from functools import reduce
from itertools import combinations


def xnor(n1, n2, bit):
    num = [0]*bit
    for i in range(bit):
        num[i] = '1' if n1[i]==n2[i] else '0'
    return ''.join(num)


def binary(number):
    i = 0
    b = ''
    while i != bit:
        b = str(number % 2) + b
        number //= 2
        i += 1
    return b


def btn(binary_num):
    return sum(int(binary_num[i])<<(bit-1-i) for i in range(bit))


n, bit = map(int, input().split())
ls = list(map(binary,map(int,input().split())))
combis = combinations(range(n+1), 2)
max_xnor = 0
for x, y in combis:
    if y-x > 1:
        value = reduce(lambda x, y: xnor(x,y,bit), ls[x:y])
    else:
        value = ls[x]
    int_value = btn(value)
    if max_xnor < int_value:
        max_xnor = int_value
print(max_xnor)

'''
5 3
1 2 3 4 5
'''
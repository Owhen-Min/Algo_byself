from functools import lru_cache


@lru_cache(maxsize=None)
def inf_comb(num):
    if num == 0:
        return 1
    else:
        return inf_comb(num//p) + inf_comb(num//q)

n, p, q = map(int,input().split())

print(inf_comb(n))
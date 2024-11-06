from itertools import combinations


n, m = map(int,input().split())
ls = [0]+list(map(int,input().split()))
for i in range(1, n+1):
    ls[i] += ls[i-1]
poss_comb = combinations(range(1,n), m-1)
ans = 10e12
for comb in poss_comb:
    comb = [0] + list(comb) + [n]
    max_val = 0
    for i in range(1,len(comb)):
        val = ls[comb[i]]-ls[comb[i-1]]
        if max_val < val:
            if val > ans:
                break
            max_val = val
    else:
        if max_val < ans:
            ans = max_val
print(ans)

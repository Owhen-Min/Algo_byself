from collections import Counter

def solution(cost, hint):
    n = len(cost)
    min_cost = anchor = sum(cost[i][0] for i in range(n))
    
    for i in range(n):
        for j in range(1,n):
            cost[i][j] -= cost[i][0]
    
    for i in range(1<<(n-1)):
        ct = Counter()
        payed = 0
        for j in range(n-1):
            if i & (1<<j):
                c, *hints = hint[j]
                payed += c
                ct.update(hints)
    
        for k in ct:
            payed += cost[k-1][min(n-1,ct[k])]
            
        min_cost = min(min_cost, payed)
    return anchor + min_cost
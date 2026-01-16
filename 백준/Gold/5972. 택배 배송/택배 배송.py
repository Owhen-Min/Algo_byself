import sys
input = sys.stdin.readline

from heapq import heappush, heappop, heapify


n, m = map(int,input().split())

djk = [50000000] * (n+1)

roads = {i: [] for i in range(n+1)}

for _ in range(m):
    a, b, c = map(int,input().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

poss = [(c, 1, b) for b, c in roads[1]]
heapify(poss)
djk[1] = 0

while poss:
    cost, st, nxt = heappop(poss)
    if djk[nxt] > djk[st]+cost:
        djk[nxt] = djk[st]+cost
        for further, cost in roads[nxt]:
            heappush(poss, (cost, nxt, further))

print(djk[n])
import heapq
from collections import defaultdict


V, e = map(int,input().split())
k = int(input())
vectors = defaultdict(list)
costs = {i:float('inf') for i in range(1, V+1)}
costs[k] = 0

for i in range(e):
    u, v, w = map(int,input().split())
    vectors[u].append((v, w))

togo =[(0, k)]

while togo:
    current_cost, node = heapq.heappop(togo)
    for neighbor, weight in vectors[node]:
        new_cost = current_cost + weight
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            heapq.heappush(togo, (new_cost, neighbor))

for i in range(1, V+1):
    if costs[i] != float('inf'):
        print(costs[i])
    else: print('INF')
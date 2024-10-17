from collections import defaultdict
import heapq


N = int(input())
M = int(input())
costs = [0] * (N+1)
heap = []
adjl = defaultdict(list)
for i in range(M):
    s, e, c = map(int, input().split())
    adjl[s].append((c, e))
curr, target = map(int,input().split())
heap.append((0, curr, curr))
flag = False
while heap:
    cost, curr, next = heapq.heappop(heap)
    curr_cost = costs[curr]
    if curr == target:
        continue
    elif not flag or costs[target] > curr_cost:
        if not costs[next] or costs[next] > curr_cost + cost:
            costs[next] = curr_cost + cost
            if next == target:
                flag = True
            else:
                for c, n in adjl[next]:
                    heapq.heappush(heap,(c, next, n))
    else:
        continue


print(costs[target])
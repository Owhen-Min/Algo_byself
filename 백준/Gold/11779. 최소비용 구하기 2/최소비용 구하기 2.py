import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

n = int(input())
m = int(input())

to_go = []
visited = [0] * (n+1)
costs = [int(1e9)] * (n+1)
poss_dict = {i: [] for i in range(1, n+1)}

for _ in range(m):
    start, end, cost = map(int,input().split())
    poss_dict[start].append((cost, start, end))

sp, ep = map(int,input().split())
costs[sp] = 0

heap = poss_dict[sp]
heapify(heap)

curr = sp
nxt = 0

while heap:
    cost, curr, nxt = heappop(heap)

    if costs[nxt] > costs[curr] + cost:
        costs[nxt] = costs[curr] + cost
        visited[nxt] = curr
        for nxxt in poss_dict[nxt]:
            heappush(heap, nxxt)

curr = ep
print(costs[curr])

track = [curr]
while curr != sp:
    track.append(visited[curr])
    curr = visited[curr]

print(len(track))
track.reverse()
print(*track)
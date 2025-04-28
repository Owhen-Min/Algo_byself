from collections import defaultdict, deque

a, b = map(int,input().split())
n, m = map(int,input().split())
dd = defaultdict(set)

for _ in range(m):
    n1, n2 = map(int,input().split())
    dd[n1].add(n2)
    dd[n2].add(n1)

q = deque([(a,0)])
visited = set()
ans = -1

while q:
    curr, cost = q.popleft()
    if curr == b:
        ans = cost
        break
    q.extend(((next, cost+1) for next in dd[curr] if next not in visited) )
    visited.update(dd[curr])

print(ans)
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())

shelters = [0] + list(map(int,input().split()))
# graph[a] = a에서 출발할 수 있는 다른 쉼터들
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    if shelters[a] > shelters[b]:
        graph[b].append(a)
    else:
        graph[a].append(b)

visited = [1 if not a else 0 for a in graph]

q = deque(i for i in range(1,n+1) if not visited[i])

while q:
    curr = q.popleft()
    flag = False
    if all(visited[nxt] for nxt in graph[curr]):
        visited[curr] = max(visited[nxt] for nxt in graph[curr]) + 1
    else:
        q.append(curr)

print("\n".join(map(str,visited[1:])))
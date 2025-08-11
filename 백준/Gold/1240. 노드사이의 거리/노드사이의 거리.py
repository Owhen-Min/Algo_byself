n, m = map(int,input().split())

# 인접그래프 생성
edges = dict()
for i in range(1,n+1):
    edges[i] = []
for _ in range(n-1):
    node1, node2, cost = map(int,input().split())
    edges[node1].append((node2, cost))
    edges[node2].append((node1, cost))

# dists[시작노드][끝노드] = 시작노드에서 끝노드로 가는 거리
dists = [[10000000]*(n+1) for _ in range(n+1)]
dists[0] = []

def djk(node):
    from collections import deque
    dists[node][node] = 0
    q = deque([node])

    while q:
        curr = q.popleft()
        curr_cost = dists[node][curr]
        for nxt, dist in edges[curr]:
            if dists[node][nxt] == 10000000:
                 dists[node][nxt] = curr_cost + dist
                 q.append(nxt)

for i in range(1,n+1):
    djk(i)

for j in range(m):
    a, b = map(int,input().split())
    print(dists[a][b])
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 인접 리스트 생성
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

LOG = 10  # 2^10 = 1024 > 1000
parent = [[0]*(N+1) for _ in range(LOG)]
depth = [0]*(N+1)
dist = [0]*(N+1)  # 루트로부터의 거리

# 2. DFS로 depth, parent[0], dist 계산
def dfs(v, p):
    for nxt, w in edges[v]:
        if nxt != p:
            depth[nxt] = depth[v] + 1
            parent[0][nxt] = v
            dist[nxt] = dist[v] + w
            dfs(nxt, v)

dfs(1, 0)  # 루트를 1로 설정

# 3. parent[k] 채우기
for k in range(1, LOG):
    for v in range(1, N+1):
        parent[k][v] = parent[k-1][parent[k-1][v]]

# 4. LCA 함수
def lca(a, b):
    # 깊이 맞추기
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[k][a]

    if a == b:
        return a

    # 위로 올리기
    for k in reversed(range(LOG)):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

# 5. 쿼리 처리
for _ in range(M):
    a, b = map(int, input().split())
    c = lca(a, b)
    print(dist[a] + dist[b] - 2 * dist[c])

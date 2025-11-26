import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
s, c, h = map(int, input().split())
s -= 1;
c -= 1;
h -= 1

# 그래프 구성
graphs = [[] for _ in range(n)]
for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    graphs[n1 - 1].append(n2 - 1)
    graphs[n2 - 1].append(n1 - 1)

# 특수 케이스: 모두 같은 위치
if s == c == h:
    print(0)
    exit()


# c를 루트로 하는 트리에서 각 노드의 레벨과 부모 구하기
def bfs_from_root(root):
    level = [-1] * n
    parent = [-1] * n
    level[root] = 0
    parent[root] = -1

    q = deque([root])
    while q:
        cur = q.popleft()
        for nxt in graphs[cur]:
            if level[nxt] == -1:
                level[nxt] = level[cur] + 1
                parent[nxt] = cur
                q.append(nxt)

    return level, parent


level, parent = bfs_from_root(c)


# s와 h의 LCA(최소 공통 조상) 찾기
def find_lca(a, b, level, parent):
    # a를 더 깊은 노드로 만들기
    if level[a] < level[b]:
        a, b = b, a

    # 같은 레벨로 맞추기
    while level[a] != level[b]:
        a = parent[a]

    # 동시에 올라가면서 LCA 찾기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


lca = find_lca(s, h, level, parent)

# 각 구간의 거리 계산
A = level[c] - level[lca]  # lca에서 c까지의 거리
B = level[lca] - level[s]  # s에서 lca까지의 거리 (음수를 양수로)
C = level[lca] - level[h]  # h에서 lca까지의 거리 (음수를 양수로)

# 실제로는 거리의 절댓값
A = abs(A)
B = abs(B)
C = abs(C)

# 순서쌍 개수 계산
ans = 0

# A 구간 내 순서쌍 (왕복하므로 순서 있는 쌍)
ans += A * (A - 1)

# B 구간 내 순서쌍 (한 방향만 가므로)
ans += B * (B - 1) // 2

# C 구간 내 순서쌍 (한 방향만 가므로)
ans += C * (C - 1) // 2

# 서로 다른 구간 간의 순서쌍
ans += B * A  # B와 A 구간
ans += B * C  # B와 C 구간
ans += A * C  # A와 C 구간

# lca와 각 구간의 순서쌍
ans += A * 2  # lca와 A 구간 (왕복)
ans += B  # lca와 B 구간
ans += C  # lca와 C 구간

print(ans)
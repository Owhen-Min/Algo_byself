import sys
input = sys.stdin.readline

n, m = map(int, input().split())
shelters = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# 방향 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    if shelters[a] > shelters[b]:
        graph[a].append(b)
        indegree[b] += 1
    else:
        graph[b].append(a)
        indegree[a] += 1

# dp[i] = i번 쉼터까지 이동 가능한 최대 거리
dp = [1] * (n + 1)

# 위상정렬
q = [i for i in range(1, n + 1) if indegree[i] == 0]

while q:
    curr = q.pop()
    for nxt in graph[curr]:
        dp[nxt] = max(dp[nxt], dp[curr] + 1)
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print("\n".join(map(str, dp[1:])))
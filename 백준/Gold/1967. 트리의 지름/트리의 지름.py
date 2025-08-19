from collections import defaultdict
import sys
sys.setrecursionlimit(50000)

# n : 노드의 개수
n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    mother, child, c = map(int,input().split())
    graph[mother].append((child,c))

# dp[node] = [node에서 나오는 최장거리 경로, [node에서 나올 수 있는 최장거리 ]
dp = [[] for _ in range(n+1)]


def dfs(node, cost):
    if dp[node]:
        return dp[node][0] + cost
    ls = list(dfs(next, c) for next, c in graph[node])
    if ls:
        dp[node]=[max(ls), ls]
    else:
        dp[node]= [0,[]]
    return dp[node][0] + cost

dfs(1, 0)
# dp = [[], [28, [15, 28]], [12, [12]], [26, [26, 19]], [7, [1, 7]], [15, [15, 4]], [10, [6, 10]], [0, []], [0, []], [0, []], [0, []], [0, []], [0, []]]

max_distance = 0
for i in range(1, n+1):
    max_distance = max(max_distance, sum(sorted(dp[i][1],reverse=True)[:2]))

print(max_distance)
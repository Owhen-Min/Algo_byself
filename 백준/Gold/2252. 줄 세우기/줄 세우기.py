from collections import defaultdict, deque
import sys
input = sys.stdin.readline


n, m = map(int,input().split())
# 인접 그래프 생성
graph = defaultdict(list)
# 위상 정렬을 위한 진입 차수를 기록할 indegree
indegree = [0]*(n+1)

for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    indegree[e] += 1

# 진입차수가 0인 (얘보다 더 작을 애가 없는) 애들은 다 때려 넣는다
q = deque(i for i in range(1,n+1) if indegree[i] == 0)
ans = []

while q:
    curr = q.popleft()
    ans.append(curr)

    for nxt in graph[curr]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(*ans)
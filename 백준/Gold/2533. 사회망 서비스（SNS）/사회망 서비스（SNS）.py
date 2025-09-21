import sys
# from array import array
input = sys.stdin.readline

n = int(input())

# graph = 인접그래프 / entries = 진입차수
graph = [[] for _ in range(n+1)]
entries = [0]*(n+1)

for _ in range(n-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    entries[x]+= 1
    entries[y]+= 1

# 진입차수가 1인 리프노드들부터 탐색하면서 올라간다.
stack = [i for i in range(1, n+1) if entries[i] == 1]

# early = i번째 사람이 얼리어뎁터인지 기록
early = [0]*(n+1)

while stack:
    curr = stack.pop()
    is_early = early[curr]
    for nxt in graph[curr]:
        entries[nxt] -= 1
        # 리프 노드를 잘라나가면서 새로운 리프노드가 발견되면 stack에 추가
        if entries[nxt] == 1:
            stack.append(nxt)
        # 해당 리프 노드가 얼리어뎁터가 아니면 부모노드는 얼리어뎁터여야 함.
        if not is_early:
            early[nxt] = 1

print(sum(early))
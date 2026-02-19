import sys
input = sys.stdin.readline
from collections import deque

n, p, k = map(int,input().split())
edges = [dict() for _ in range(n+1)]

for _ in range(p):
    a, b, c = map(int,input().split())
    edges[a][b] = c
    edges[b][a] = c


ans = 1000001
left, right = 0, 1000000

# 결정문제 : 정해진 코스트 안에서 조건을 달성하는지 확인하기
while left <= right:
    mid = (left+right)//2

    # 정해진 코스트보다 큰 숫자들의 갯수를 구하는 다익스트라
    costs = [1000001]*(n+1)
    costs[1] = 0
    
    # 1에서 시작하기
    q = deque([1])

    while q:
        curr = q.popleft()
        for nxt, cost in edges[curr].items():
            if cost <= mid and costs[nxt] > costs[curr]:
                costs[nxt] = costs[curr]
                q.append(nxt)
            elif costs[nxt] > costs[curr]+1:
                costs[nxt] = costs[curr]+1
                q.append(nxt)


    if costs[n] <= k:
        ans = mid
        right = mid-1
    else:
        left = mid+1

print(-1 if ans == 1000001 else ans)
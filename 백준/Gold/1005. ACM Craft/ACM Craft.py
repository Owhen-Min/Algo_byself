import sys

input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())

    dp = [0] * (n + 1)
    times = [0] + list(map(int, input().split()))

    # 그래프 구성
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for __ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)  # x -> y
        indegree[y] += 1  # y의 진입 차수 증가

    target = int(input())

    # 위상 정렬 시작
    queue = deque()

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i]  # 시작 노드의 시간 초기화

    # 위상 정렬 수행
    while queue:
        curr = queue.popleft()

        for nxt in graph[curr]:
            # 현재 노드를 거쳐가는 경우의 시간을 계산
            dp[nxt] = max(dp[nxt], dp[curr] + times[nxt])

            # 진입 차수 감소
            indegree[nxt] -= 1

            # 진입 차수가 0이 되면 큐에 삽입
            if indegree[nxt] == 0:
                queue.append(nxt)

    print(dp[target])
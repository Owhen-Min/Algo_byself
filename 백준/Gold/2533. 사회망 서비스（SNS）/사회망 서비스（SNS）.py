import sys
from array import array
input = sys.stdin.readline

n = int(input())
graph = [array("i") for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# dp[i][0] = i번째 노드가 얼리어답터가 아닐 때 조건을 충족하는 최소한의 얼리어답터수
# dp[i][1] = i번째 노드가 얼리어답터일 때 조건을 충족하는 최소한의 얼리어답터수
dp = [[0,0] for _ in range(n+1)]

# stack.pop() = 현재 위치, 부모노드, 자식노드의 계산이 끝났는지 여부
stack = [(1, -1, False)]

while stack:
    curr, parent, flag = stack.pop()
    # 만약 자식 노드들을 다 방문하지 않아서 최소값을 모르는 경우, 다음에 오라고 놓아주기
    if not flag:
        stack.append((curr, parent, True))
        for child in graph[curr]:
            if child != parent:
                stack.append((child, curr, False))
    # 자식들의 노드 방문이 끝난 후 계산
    else:
        dp[curr][0] = 0
        dp[curr][1] = 1
        for child in graph[curr]:
            if child != parent:
                # 내가 얼리어답터가 아닌 경우 자식은 꼭 얼리어답터여야 함
                dp[curr][0] += dp[child][1]
                # 내가 얼리어답터일 경우 자식은 더 작은 애로 가져오면 됨
                dp[curr][1] += min(dp[child][0], dp[child][1])

print(min(dp[1]))
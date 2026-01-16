import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# order[i] = i번 문제를 풀고난 뒤 풀 수 있는 후행 문제들 리스트
order = {i: [] for i in range(1,n+1)}
# procedure[i] = i번 문제를 풀기 전 풀어야 하는 선행문제 개수
procedure = [0]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    order[a].append(b)
    procedure[b] += 1

ans = []
q = [i for i in range(1,n+1) if procedure[i] < 1]
heapq.heapify(q)

while q:
    curr = heapq.heappop(q)
    ans.append(curr)
    # 문제를 풀었으니 후행문제들을 확인하고 큐에 넣는다.
    for nxt in order[curr]:
        procedure[nxt] -= 1
        if procedure[nxt] == 0:
            heapq.heappush(q, nxt)

print(*ans)
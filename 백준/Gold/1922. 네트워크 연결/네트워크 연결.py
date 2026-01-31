import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parents = [i for i in range(n+1)]

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(p1, p2):
    parents[max(p1, p2)] = min(p1, p2)

graphs = sorted((c, a, b) for _ in range(m) for a, b, c in [map(int,input().split())])
ans = 0
idx = 0
# 연결이 되지 않은 노드의 개수는 n-1이므로 n을 계속 차감해주면서 연결되지 않은 노드의 개수를 카운트하면 된다.
n -= 1

while n:
    cost, a, b = graphs[idx]
    pa, pb = find(a), find(b)
    if pa != pb:
        union(pa, pb)
        ans += cost
        n -=1

    idx += 1

print(ans)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(n1, n2):
    if n1 < n2:
        parents[n2] = parents[n1]
    else:
        parents[n1] = parents[n2]
    return

parents = [i for i in range(n)]

ans= 0

for i in range(1,m+1):
    n1,n2 = map(int,input().split())
    p1, p2 = find(n1), find(n2)

    if p1 == p2:
        ans = i
        break
    union(p1, p2)

print(ans)
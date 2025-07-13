import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int,input().split())
parents = [i for i in range(n+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x_p = find(x)
    y_p = find(y)
    if x_p > y_p:
        parents[x_p] = y_p
    else:
        parents[y_p] = x_p

for _ in range(m):
    command, a, b = map(int,input().split())

    if command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def union(n1, n2):
    parents[n2] = n1

def find(n):
    if parents[n] == n:
        return n
    else:
        parents[n] = find(parents[n])
        return parents[n]

v, e = map(int,input().split())
parents = [i for i in range(v+1)]
q = []
linked = 1

ans = 0

for _ in range(e):
    s, e, w = map(int,input().split())
    heapq.heappush(q, (w, s, e))

while linked != v:
    w, s, e = heapq.heappop(q)
    s = find(s)
    e = find(e)
    if s != e:
        union(s, e)
        ans += w
        linked += 1

print(ans)
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


n,m = map(int,input().split())
taller = defaultdict(list)
shorter = defaultdict(list)
ls = [0]*(n+1)

for _ in range(m):
    s, e = map(int,input().split())
    taller[s].append(e)
    shorter[e].append(s)
    ls[e] += 1

ans = []
temp = []
def lining(node):
    while True:
        if ls[node] == -1:
            return
        elif ls[node] == 0:
            temp.append(node)
            ls[node] = -1
            for nxt in taller[node]:
                ls[nxt] -= 1
            return
        else:
            for nxt in shorter[node]:
                lining(nxt)

for i in range(1,n+1):
    temp = []
    lining(i)
    ans += temp

print(' '.join(map(str, ans)))
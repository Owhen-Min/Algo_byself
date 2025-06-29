import sys
input = sys.stdin.readline

n, m = map(int,input().split())
grounds = list(map(int,input().split()))
imos = [0]*n

for _ in range(m):
    s, e, a = map(int,input().split())
    imos[s-1] += a
    try:
        imos[e] -= a
    except IndexError:
        pass

cs = 0

for i in range(n):
    cs += imos[i]
    grounds[i] += cs

print(*grounds)
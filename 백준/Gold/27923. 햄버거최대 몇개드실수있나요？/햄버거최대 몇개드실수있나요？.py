import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

effect = [0]*(n)
for i in map(int, input().split()):
    effect[i-1]+=1
    if i+l <= n:
        effect[i+l-1] -= 1

for i in range(1,n):
    effect[i] += effect[i-1]
effect.sort()

result = sum(h[j] >> effect[j] for j in range(n) if effect[j] <64)
print(result)
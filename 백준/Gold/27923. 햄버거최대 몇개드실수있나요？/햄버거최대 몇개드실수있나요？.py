import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
h_list = sorted(list(map(int, input().split())))

effect = [0]*n
for i in map(int, input().split()):
    effect[i-1]+=1
    if i+l <= n:
        effect[i+l-1] -= 1

for i in range(1,n):
    effect[i] += effect[i-1]
effect.sort()


result = 0
for j in range(n):
    if effect[j]<64: #포인트임
        result += h_list[j]>>effect[j]
print(result)
import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
h_list = sorted(list(map(int, input().split())))

tmp = [0]*(n+1)
for i in map(int, input().split()):
    tmp[i]+=1
for i in range(1,n+1):
    tmp[i] +=tmp[i-1]

effect = [0]*n
for i in range(1,n+1):
    if i<l:
        effect[i-1] = tmp[i]
    else:
        effect[i-1] = tmp[i]-tmp[i-l]
effect.sort()


result = 0
for j in range(n):
    if effect[j]<64: #포인트임
        result += h_list[j]>>effect[j]
print(result)
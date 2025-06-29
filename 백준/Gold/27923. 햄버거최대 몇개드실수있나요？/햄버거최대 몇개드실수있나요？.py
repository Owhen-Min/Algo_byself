import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())

diff = [0]*n

m = sorted(map(int, input().split()))

for num in map(int,input().split()):
    diff[num-1] += 1
    
    if num+l <=n:
        diff[num+l-1] -= 1
    
for i in range(n-1):
    diff[i+1] += diff[i]

diff.sort()

print(sum(a>>coke for a, coke in zip(m, diff)))
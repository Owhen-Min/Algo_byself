import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = sorted(int(input()) for _ in range(n))

start, end = 0, 0
ans = 2e9

while start <= end < n:
    diff = arr[end]-arr[start]
    if diff >= m:
        if ans > diff:
            ans = diff
        start += 1
    else:
        end += 1

print(ans)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = sorted(tuple(map(int, input().split())) for _ in range(n))

dp = [0] * (k+1)

for w, v in arr:
    for j in range(k,w-1, -1): #무게
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[k])
n, k = map(int,input().split())

dp = [k+1]*(k+1)
dp[0] = 0

coins = [int(input()) for _ in range(n)]

for i in range(k+1):
    if dp[i] != k+1:
        for coin in coins:
            if i+coin <= k:
                dp[i+coin] = min(dp[i]+1, dp[i+coin])
                
if dp[-1] == k+1:
    print(-1)
else: print(dp[-1])
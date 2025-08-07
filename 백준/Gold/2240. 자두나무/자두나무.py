import sys
input = sys.stdin.readline

t, w = map(int,input().split())
plums = [int(input()) for _ in range(t)]

dp = [[0]*(w+1) for _ in range(t+1)]

for i in range(1,t+1):
    if plums[i-1] == 1:
        dp[i][0] = dp[i-1][0]+1
        for j in range(2,w+1,2):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+1
        for k in range(1,w+1,2):
            dp[i][k] = dp[i-1][k]
    else:
        for j in range(0,w+1,2):
            dp[i][j] = dp[i-1][j]
        for k in range(1,w+1,2):
            dp[i][k] = max(dp[i-1][k-1], dp[i-1][k])+1

print(max(dp[t]))
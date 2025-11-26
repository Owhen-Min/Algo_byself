n = int(input())
ls = tuple(map(int,input().split()))
c = int(input())
accu_len = n-c+1
accu = [0] * accu_len

acc = sum(ls[:c])
accu[0] = acc

for i in range(1, accu_len):
    acc += ls[i+c-1] - ls[i-1]
    accu[i] = acc

dp = [[0]*accu_len for _ in range(3)]

dp[0][0] = accu[0]
for i in range(1,accu_len):
    curr = accu[i]
    dp[0][i] = max(curr, dp[0][i-1])
    if i-c>=0:
        dp[1][i] = max(dp[1][i-1], dp[0][i-c] + curr)
        if i-2*c>=0:
            dp[2][i] = max(dp[2][i-1], dp[1][i-c] + curr)

print(dp[2][accu_len-1])
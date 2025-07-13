import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

# 길이 1짜리 팰린드롬
for i in range(n):
    dp[i][i] = 1

# 길이 2 이상
for length in range(2, n+1):
    for start in range(n - length + 1):
        end = start + length - 1
        if ls[start] == ls[end]:
            if length == 2:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

m = int(input())
ans = [0]*m
for _ in range(m):
    s, e = map(int, input().split())
    ans[_] = dp[s-1][e-1]

print("\n".join(map(str,ans)))

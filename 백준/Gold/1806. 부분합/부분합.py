n, s = map(int,input().split())
ls = list(map(int,input().split()))

i, j = 0, 0
hap = ls[0]
ans = n+1
while True:
    if hap < s:
        j += 1
        if j == n: break
        else: hap += ls[j]
    else:
        hap -= ls[i]
        ans = min(ans, j-i+1)
        i += 1

if ans == n+1:
    ans = 0

print(ans)
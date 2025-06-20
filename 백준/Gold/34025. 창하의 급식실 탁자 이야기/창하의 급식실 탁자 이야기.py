import sys
input = sys.stdin.readline

n = int(input())
ans = -1
cnt = 0
ls = []

for _ in range(n):
    value = int(input())
    if value %2:
        if value == 1:
            cnt += 1
        else:
            ls.append(value)
    else:
        ans += value//2+1

flag = False

if cnt:
    if ans:
        ans += cnt +1
    else:
        ans += cnt
    flag = True
    if ls and not len(ls)%2:
        ans -=1

for odd in ls:
    if flag:
        ans += odd//2+1
    else:
        ans += odd//2+2
    flag = not flag

print(ans)
n, s = map(int,input().split())
seq = list(map(int,input().split()))
hap = seq[0]
left = 0
right = 1
ans = 10e9

while True:
    if hap >= s:
        ans = min(ans, right-left)
        hap -= seq[left]
        left += 1
    else:
        if right == n:
            break
        hap += seq[right]
        right += 1

if ans == 10e9:
    print(0)
else:
    print(ans)


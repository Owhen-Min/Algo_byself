T = int(input())
for tc in range(T):
    x, y = map(int,input().split())
    dist = y-x
    cnt = 0
    i = 1
    while dist > 0:
        if dist <= i:
            cnt += 1
            break
        dist -= 2*i
        cnt += 2
        i += 1
    print(cnt)
T = int(input())
for tc in range(1,T+1):
    a, b, N = map(int,input().split())
    cnt = 0
    while a <= N and b <= N:
        if a>b: b+= a
        else: a += b
        cnt += 1
    print(cnt)

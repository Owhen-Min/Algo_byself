T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for _ in range(N):
        n1, n2 = map(int,input().split())
        cnt += n2-n1+1
    print(f'#{tc} {cnt}')
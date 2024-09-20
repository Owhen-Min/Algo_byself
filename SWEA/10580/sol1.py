T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ls = [[] for _ in range(N)]
    cnt = 0

    for i in range(N):
        ls[i] = list(map(int,input().split()))

    for i in range(N-1):
        for j in range(i+1, N):
            if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]: pass
            elif ls[i][0] > ls[j][0] and ls[i][1] > ls[j][1]: pass
            else: cnt +=1
    print(f'#{tc} {cnt}')
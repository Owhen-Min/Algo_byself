T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    c_ls = sorted(list(map(int,input().split())))
    for i in range(N):
        if c_ls[i]//M * K - (i+1) < 0:
            print(f'#{tc} Impossible')
            break
    else: print(f'#{tc} Possible')
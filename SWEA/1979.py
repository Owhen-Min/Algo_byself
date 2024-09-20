T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    delta = list(range(1,K))
    count = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                checker = True
                for d in delta:
                    if i+d >= N:
                        checker = False
                        break
                    else:
                        if puzzle[i+d][j] == 0:
                            checker = False
                            break
                        else:
                            if i+K < N and puzzle[i+K][j] == 1:
                                checker = False
                                break
                if checker and (i==0 or puzzle[i-1][j]==0) : count += 1
                checker = True
                for d in delta:
                    if j + d >= N:
                        checker = False
                        break
                    else:
                        if puzzle[i][j+d] == 0:
                            checker = False
                            break
                        else:
                            if j+K < N and puzzle[i][j+K] == 1:
                                checker = False
                                break
                if checker and (j==0 or puzzle[i][j-1]==0): count += 1
    print(f'#{tc} {count}')

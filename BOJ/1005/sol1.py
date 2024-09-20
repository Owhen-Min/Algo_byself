for tc in range(1, 11):
    N = int(input())
    board= [input().split() for _ in range(N)]
    cnt = 0
    for i in range (N):
        key = ''
        for j in range(N):
            if board[j][i] != '0':
                key += board[j][i]
        cnt += key.count('12')
    print(f'#{tc} {cnt}')

T = int(input())
delta = [[1,0], [-1,0],[0,1], [0,-1], [1,1], [1,-1], [-1,-1], [-1,1]]
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = [[0]*(N+1) for _ in range(N+1)]
    board[N // 2][N // 2] = board[N // 2+1][N // 2+1] = 2
    board[N // 2 + 1][N // 2] = board[N // 2][N // 2 + 1] = 1
    for _ in range(M):
        x, y , color = map(int,input().split())
        board[y][x] = color
        for dx, dy in delta:
            c_list = [[0] * N]
            x_c, y_c = x + dx, y + dy
            idx = 1
            while 0 < x_c <= N and 0 < y_c <= N and board[y_c][x_c] != 0:
                if board[y_c][x_c] == color:
                    for _ in range(idx-1):
                        x_c, y_c = x_c - dx, y_c - dy
                        board[y_c][x_c] = color
                    break
                x_c, y_c = x_c+dx, y_c+dy
                idx += 1
    b_count = 0
    w_count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1: b_count += 1
            elif board[i][j] == 2: w_count += 1
    print(f'#{tc}', b_count, w_count)
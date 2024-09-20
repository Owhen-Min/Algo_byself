T = int(input())

for tc in range (1, T+1):
    N = int(input())
    print(f'#{tc}')
    board = [ [0]*N for _ in range(N)]
    for y in range(N+1):
        for x in range(y+1):
            if y == 0:
                board[y][x] = 1
            elif x == 0:
                board[y][x] = 1
            else:
                board[y][x] = board[y-1][x] + board[y-1][x-1]

    for i in range(N):
        for j in range(i+1):
            print(board[i][j], end= ' ')
        print()
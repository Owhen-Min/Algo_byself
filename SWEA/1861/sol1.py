deltas = ((1,0),(-1,0),(0,1),(0,-1))

def go(y, x, curr_len = 1):
    global max_i, max_len

    if max_len < curr_len:
        max_len = curr_len
        max_i = board[i][j]
    elif max_len == curr_len:
        if max_i > board[y][x]:
            max_i = board[i][j]

    for dy, dx in deltas:
        if 0<=y+dy<N and 0<=x+dx<N:
            if board[y][x] + 1 == board[y+dy][x+dx]:
                go(y+dy,x+dx,curr_len+1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    max_len = 0
    max_i = 10000
    for i in range(N):
        for j in range(N):
            go(i, j)

    print(f'#{tc} {max_i} {max_len}')
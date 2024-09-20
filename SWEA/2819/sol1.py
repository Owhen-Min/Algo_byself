deltas = ((1,0),(-1,0),(0,1),(0,-1))


def move(curr, s, depth=0):
    global n_set, visited

    if depth == 6:
        n_set.add(s)
        return

    y, x = curr
    record = str(y)+str(x)+s+str(depth)

    if record in visited:
        return
    else: visited.add(record)

    for dy, dx in deltas:
        if 0<=y+dy<4 and 0<=x+dx<4:
            move(((y + dy), (x + dx)), s + board[y + dy][x + dx], depth + 1)




T = int(input())
for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    n_set = set()
    visited = set()
    for i in range(4):
        for j in range(4):
            move((i,j),board[i][j])

    print(f'#{tc} {len(n_set)}')
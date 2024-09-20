T = int(input())
for tc in range (1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    x = 0
    y = 0
    size = N
    dir = 0 # 방향이 우측일 때 0, 아래쪽일 때 1, 왼쪽일 때 2, 윗쪽일 때 3
    dir_d = [[1, 0],[0,1],[-1,0],[0,-1]] # 방향에 맞게 x, y값을 수정해주는 delta값
    dx, dy = dir_d[0]

    for i in range(1,N**2+1): # N의 제곱의 숫자까지 넣어야 하므로 N**2+1
        snail[y][x] = i

        if x + dx == N or y + dy == N or snail[y+dy][x+dx] !=0: # x나 y가 index를 넘어갈 경우 또는 가려는 방향에 숫자가 차 있는 경우 방향을 바꾼다
            dir = (dir+1) % 4
            dx, dy = dir_d[dir]

        x += dx 
        y += dy

    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])

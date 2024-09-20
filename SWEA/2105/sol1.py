# 우하단, 좌하단, 좌상단, 우상단, 한바퀴를 돌 때를 위해서 제자리인 0
delta = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 0]]

# 돌아왔다는 것을 확인하기 위한 시작지점값, 현재 지점값 curr
# 가고있는 방향을 체크하는 dir, 여태까지 먹은 디저트를 담는 set
def tour(start,curr,dessert, dir=0):
    if dessert and curr == start:
        global max_desserts
        if max_desserts < len(dessert):
            max_desserts = len(dessert)

    elif dir == 4:
        return

    y, x = curr
    if 0 <= y < N and 0 <= x < N:
        if desserts[y][x] in dessert:
            return
        else: dessert.add(desserts[y][x])

        tour(start, (y+delta[dir][0], x+delta[dir][1]),dessert, dir)
        tour(start, (y+delta[dir+1][0], x+delta[dir+1][1]),dessert, dir+1)
        dessert.discard(desserts[y][x])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    desserts = [list(map(int,input().split())) for _ in range(N)]
    max_desserts = -1
    for i in range(N-2):
        for j in range(1,N-1):
            tour((i,j),(i,j), set())

    print(f'#{tc} {max_desserts}')
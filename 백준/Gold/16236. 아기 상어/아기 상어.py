from collections import deque


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

# fishes[i]: i 크기를 가진 물고기들의 좌표들
fishes = {2:[],3:[],4:[],5:[],6:[], 7:[]}
# poss: 먹을 수 있는 물고기들의 숫자를 담은 변수. 0일 경우 탐색을 멈춘다.
poss = 0

for i in range(n):
    for j in range(n):
        temp = board[i][j]
        if not temp:
            continue
        elif temp == 1:
            poss += 1
        elif temp == 2:
            fishes[temp].append((i, j))
        elif temp == 9:
            q = deque([(i,j,0)])
            board[i][j] = 0
        else:
            fishes[temp].append((i,j))

# board[i][j]가 0일 경우 통과, 1일 경우 먹을 수 있음 2일 경우 통과할 수 있음 3일 경우 통과할 수 없음

# 문제 조건에 따라 위, 좌측을 먼저 탐색하도록 deltas 설정
deltas = [(-1,0), (0,-1), (1,0), (0,1)]

time = 0
size = 2
tp = 2

while poss:
    # 먹을 수 있는 물고기가 있다면 BFS를 돌려본다.
    visited = [[0]*n for _ in range(n)]

    # poss_targets = 최단 거리의 먹을 수 있는 물고기 좌표들
    poss_targets = []
    shortest_time = -1

    while q:
        y, x, ct = q.popleft()

        # 해당 좌표가 최단거리가 아니기 시작하면 탐색을 멈춘다.
        if shortest_time != -1 and shortest_time < ct+1:
            break

        for dy, dx in deltas:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<n and board[ny][nx] <= 2 and visited[ny][nx] == 0:
                if board[ny][nx] == 1:
                    shortest_time = ct+1
                    visited[ny][nx] = 1
                    poss_targets.append((ny, nx, shortest_time))
                else:
                    visited[ny][nx] = 1
                    q.append((ny, nx, ct+1))

    # 탐색을 돌고 난 뒤 먹을 수 있는 물고기가 있는지 확인한다.
    if poss_targets:
        poss -= 1
        ny, nx, time = sorted(poss_targets, key=lambda x: (x[0], x[1]))[0]
        board[ny][nx]=0
        tp-=1
        q = deque([(ny, nx, time)])
    # 더이상 먹을 수 있는 물고기가 없다면 탐색을 멈춘다.
    else:
        break

    # 물고기를 먹었다면 상어 크기가 커지는지 확인하고 처리한다.
    while tp == 0 and size < 7:
        poss += len(fishes[size])
        for i, j in fishes[size]:
            board[i][j] = 1

        size += 1
        tp = size

        for i, j in fishes[size]:
            board[i][j] = 2

print(time)
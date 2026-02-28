# import sys
# input = sys.stdin.readline
from collections import deque
from copy import deepcopy

k = int(input())
w, h = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(h)]

# visited[j][y][x] = j번 점프한 후에 y, x에 방문한 적이 있는지 여부를 확인하는 bool
visited = [deepcopy(board) for _ in range(k+1)]

# y좌표, x좌표, 점프 횟수, 움직인 수
q = deque([(0,0,0,0)])

delta1 = ((1,0),(-1,0),(0,1),(0,-1))
delta2 = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))

while q:
    y, x, j, curr = q.popleft()
    if y == h-1 and x == w-1:
        break
    # 점프 없는 상하좌우
    for dy, dx in delta1:
        ny, nx = y+dy, x+dx
        if 0<=ny<h and 0<=nx<w and visited[j][ny][nx]==0:
            visited[j][ny][nx] = curr+1
            q.append((ny,nx,j,curr+1))

    # 말처럼 움직이기
    if j < k:
        for dy, dx in delta2:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and visited[j+1][ny][nx] == 0:
                visited[j+1][ny][nx] = curr+1
                q.append((ny, nx, j+1, curr + 1))
else:
    curr = -1

print(curr)
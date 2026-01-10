import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int,input().split())
visited = [[10000]*n for _ in range(m)]
visited[0][0] = 0
board = [list(map(int,input().strip())) for _ in range(m)]

q = deque([(0,0)])
deltas = ((1,0), (-1,0), (0,-1), (0,1))
while q:
    y, x = q.popleft()

    for dy, dx in deltas:
        ny, nx = y+dy, x+dx
        if 0<=ny<m and 0<=nx<n and visited[ny][nx] > visited[y][x] + board[ny][nx]:
            visited[ny][nx] = visited[y][x] + board[ny][nx]
            q.append((ny, nx))

print(visited[m-1][n-1])
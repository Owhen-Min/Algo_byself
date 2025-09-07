import sys
input = sys.stdin.readline

r, c = map(int,input().split())
board = list(input() for _ in range(r))
visited = [[0]*c for _ in range(r)]

# DFS 기준 위 중간 아래 순으로 탐색하도록 설정, 최적값 보장
deltas = ((1,1),(0,1),(-1,1))
ans = 0

for i in range(r):
    stack = [(i,0)]
    while stack:
        y, x = stack.pop()
        visited[y][x] = 1
        if x == c-2:
            ans += 1
            break
        for dy, dx in deltas:
            ny, nx = y+dy, x+dx
            if 0<=ny<r and board[ny][nx] == '.' and not visited[ny][nx]:
                stack.append((ny, nx))

print(ans)
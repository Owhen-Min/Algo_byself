from collections import deque


n = int(input())

board = [list(map(int,str(input()))) for _ in range(n)]
visited = [[2500] * n for _ in range(n)]

deltas = ((1,0), (-1,0), (0, 1), (0, -1))

q = deque([(0,0,0)])

while q:
    y, x, cost = q.popleft()
    if not board[y][x]:
        cost += 1

    if visited[y][x] > cost:
        visited[y][x] = cost
        for dy, dx in deltas:
            ny, nx = dy+y, dx+x
            if 0 <= ny < n and 0<= nx < n:
                q.append((ny, nx, cost))

print(visited[n-1][n-1])
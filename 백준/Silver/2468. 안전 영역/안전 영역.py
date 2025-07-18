n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
deltas = ((1,0), (-1,0), (0,1), (0,-1))
ans = 1
nums = set().union(*board)

nums = sorted(nums)[1:]

def grouping(anchor, start_y, start_x):
    stack = [(start_y,start_x)]
    visited[start_y][start_x] = anchor

    while stack:
        y, x = stack.pop()

        for dy, dx in deltas:
            ny, nx = dy+y, dx+x

            if 0<=ny<n and 0<=nx<n and board[ny][nx] >= anchor > visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = anchor

for num in nums:
    group = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] >= num > visited[i][j]:
                grouping(num, i, j)
                group += 1

    ans = max(ans, group)

print(ans)
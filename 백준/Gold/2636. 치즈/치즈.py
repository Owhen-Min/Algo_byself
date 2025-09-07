n, m = map(int,input().split())

cheezes = [list(map(int,input().split())) for _ in range(n)]

deltas = ((1,0),(-1,0),(0,-1),(0,1))

def dfs(board):
    next_melt = set()
    stack = [(0,0)]
    visited = [[0]*m for _ in range(n)]

    while stack:
        cy, cx = stack.pop()
        for dy, dx in deltas:
            ny, nx = cy+dy, cx+dx
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                if cheezes[ny][nx] == 0:
                    stack.append((ny,nx))
                    visited[ny][nx] = 1
                else:
                    next_melt.add((ny,nx))
    return next_melt

# not_melt = 녹여야 할 치즈의 수
not_melt = sum(sum(cheeze) for cheeze in cheezes)
ans = 0

while True:
    next_melt = dfs(cheezes)
    ans += 1
    if not_melt == len(next_melt):
        break
    not_melt -= len(next_melt)
    for y, x in next_melt:
        cheezes[y][x] = 0

print(ans)
print(len(next_melt))
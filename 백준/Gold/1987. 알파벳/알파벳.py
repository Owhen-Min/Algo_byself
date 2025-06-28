r, c = map(int, input().split())

board = [input() for _ in range(r)]
# 각 위치에 도달했을 때 사용한 알파벳들의 집합을 저장
visited = [[set() for _ in range(c)] for _ in range(r)]
# 시작 위치에 첫 알파벳 추가
visited[0][0].add(frozenset([board[0][0]]))
# (y, x, 지금까지 방문한 알파벳 집합)
stack = [(0, 0, frozenset([board[0][0]]))]
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 1

while stack:
    y, x, path = stack.pop()
    ans = max(ans, len(path))

    for dy, dx in deltas:
        ny, nx = y+dy, x+dx
        if 0 <= ny < r and 0 <= nx < c:
            # 다음 위치의 알파벳이 현재 경로에 없는 경우
            if board[ny][nx] not in path:
                # 새 경로 생성
                new_path = path| {board[ny][nx]}
                # 이 새 경로가 이미 이 위치에 도달한 적이 없다면 추가
                if new_path not in visited[ny][nx]:
                    visited[ny][nx].add(new_path)
                    stack.append((ny, nx, new_path))

print(ans)
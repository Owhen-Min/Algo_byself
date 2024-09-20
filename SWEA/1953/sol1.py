deltas = {
    1: ((1, 0), (-1, 0), (0, 1), (0, -1)),  # 상하좌우
    2: ((1, 0), (-1, 0)),                    # 위아래
    3: ((0, 1), (0, -1)),                    # 좌우
    4: ((-1, 0), (0, 1)),                    # 우상
    5: ((0, 1), (1, 0)),                     # 우하
    6: ((0, -1), (1, 0)),                    # 좌하
    7: ((0, -1), (-1, 0))                    # 좌상
}


def is_connected(prev_y, prev_x, curr_y, curr_x):
    # 만약 가려는 곳이 터널이 없다면 False
    if drainage[curr_y][curr_x] == 0:
        return False
    # 가려는 곳이 이전과 연결되어 있는지 판단
    dy, dx = curr_y - prev_y, curr_x - prev_x
    return (-dy, -dx) in deltas[drainage[curr_y][curr_x]]


def move(y, x, time):
    # 방문한 적이 없다면 1 표시
    if visited[y][x]:
        return
    visited[y][x] = 1

    # nx, ny가 범위를 넘지 않고 연결이 되어 있다면, 다음 칸으로 이동해서 판단
    for dy, dx in deltas[drainage[y][x]]:
        ny, nx = y + dy, x + dx
        if time < L and 0 <= ny < N and 0 <= nx < M and is_connected(y, x, ny, nx):
            move(ny, nx, time + 1)


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    drainage = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    move(R, C, 1)

    result = sum(1 for row in visited for cell in row if cell)
    print(f'#{tc} {result}')
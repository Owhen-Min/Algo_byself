deltas = {
    1: ((1, 0), (-1, 0), (0, 1), (0, -1)),  # 상하좌우
    2: ((1, 0), (-1, 0)),                    # 위아래
    3: ((0, 1), (0, -1)),                    # 좌우
    4: ((-1, 0), (0, 1)),                    # 우상
    5: ((0, 1), (1, 0)),                     # 우하
    6: ((0, -1), (1, 0)),                    # 좌하
    7: ((0, -1), (-1, 0))                    # 좌상
}

def move(y, x, time):
    # 방문한 적이 없거나 이동할 기회가 더 많이 남은 채로 해당 칸에 왔다면 시간 표시
    if visited[y][x] <= time:
        return
    visited[y][x] = time

    # nx, ny가 범위를 넘지 않고 연결이 되어 있다면, 다음 칸으로 이동해서 판단
    for dy, dx in deltas[drainage[y][x]]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and drainage[ny][nx] and (-dy, -dx) in deltas[drainage[ny][nx]]:
            move(ny, nx, time + 1)


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    drainage = [list(map(int, input().split())) for _ in range(N)]
    visited = [[21] * M for _ in range(N)]
    # L의 최대값이 20이므로 21로 둔다.

    move(R, C, 1)
    # 시뮬레이션을 돈다.

    result = sum(1 for row in visited for cell in row if cell <= L)
    # L 시간 내에 이동했던 칸들에 대해 1로 치고서 합을 구한다.

    print(f'#{tc} {result}')
def solution(game_board, table):
    from collections import defaultdict
    blanks = defaultdict(int)
    n, m = len(game_board), len(game_board[0])

    def dfs(board, start_y, start_x, is_table):
        points = [(0, 0)]
        totals = 0
        stack = [(start_y, start_x)]
        if is_table:
            board[start_y][start_x] = 0
            totals += 1
        else: board[start_y][start_x] = 1


        while stack:
            y, x = stack.pop()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y+dy, x+dx
                if 0<=ny < n and 0<=nx<m and board[ny][nx]==is_table:
                    points.append((ny-start_y, nx-start_x))
                    stack.append((ny, nx))
                    if is_table:
                        board[ny][nx] = 0
                        totals += 1
                    else:
                        board[ny][nx] = 1

        if is_table:
            return [normalize(points), normalize([(-x, y) for y, x in points]), normalize([(-y, -x) for y, x in points]), normalize([(x, -y) for y, x in points])], totals

        return normalize(points), 0

    # 모든 좌표를 0~6 안으로 들어올 수 있게 보정해서 tuple로 반환. set로 관리할 수 있음.
    def normalize(points):
        # 모든 좌표를 0~6 안으로 들어올 수 있게 보정
        pivot_y = min(point[0] for point in points)
        pivot_x = min(point[1] for point in points)
        return tuple(sorted((point[0]-pivot_y, point[1]-pivot_x) for point in points))

    for i in range(n):
        for j in range(m):
            if not game_board[i][j]:
                blank = dfs(game_board, i, j,False)[0]
                blanks[blank] += 1
    del game_board, blank

    answer = 0
    for i in range(n):
        for j in range(m):
            if table[i][j]:
                pieces, total = dfs(table, i, j, True)
                for piece in pieces:
                    if blanks[piece]:
                        blanks[piece] -= 1
                        answer += total
                        break

    return answer
def solution(game_board, table):
    from collections import defaultdict
    
    def dfs(board, start_y, start_x, target, visited):
        points = []
        stack = [(start_y, start_x)]
        visited[start_y][start_x] = True
        
        while stack:
            y, x = stack.pop()
            points.append((y, x))
            
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                ny, nx = y + dy, x + dx
                if (0 <= ny < len(board) and 0 <= nx < len(board[0]) and 
                    not visited[ny][nx] and board[ny][nx] == target):
                    visited[ny][nx] = True
                    stack.append((ny, nx))
        
        return points
    
    def normalize_shape(points):
        if not points:
            return tuple()
        min_y = min(p[0] for p in points)
        min_x = min(p[1] for p in points)
        normalized = [(p[0] - min_y, p[1] - min_x) for p in points]
        return tuple(sorted(normalized))
    
    def get_all_rotations(points):
        rotations = []
        current = points
        
        for _ in range(4):
            rotations.append(normalize_shape(current))
            # 90도 회전: (y, x) -> (-x, y)
            current = [(-p[1], p[0]) for p in current]
        
        return rotations
    
    n = len(game_board)
    
    # 빈 공간 찾기
    blanks = defaultdict(int)
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited[i][j]:
                blank_points = dfs(game_board, i, j, 0, visited)
                if blank_points:
                    # 상대 좌표로 변환
                    relative = [(p[0] - blank_points[0][0], p[1] - blank_points[0][1]) 
                               for p in blank_points]
                    shape = normalize_shape(relative)
                    blanks[shape] += 1
    
    # 조각 찾기 및 매칭
    answer = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                piece_points = dfs(table, i, j, 1, visited)
                if piece_points:
                    # 상대 좌표로 변환
                    relative = [(p[0] - piece_points[0][0], p[1] - piece_points[0][1]) 
                               for p in piece_points]
                    rotations = get_all_rotations(relative)
                    
                    # 매칭 시도
                    for rotation in rotations:
                        if blanks[rotation] > 0:
                            blanks[rotation] -= 1
                            answer += len(piece_points)
                            break
    
    return answer

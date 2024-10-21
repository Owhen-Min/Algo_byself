T = int(input())
for tc in range (1, T + 1):
    checker = True
    d = []
    board = [list(map(int, input().split())) for _ in range(9)]
    for i in range(3):
        for j in range(3):
            d.append([i,j]) # 박스 안 탐색을 위한 delta

    for r in range(9): # row에서 스도쿠 오류 있는지 탐색
        count = [0]*10
        for c in range(9):
            count[board[r][c]] += 1
        if 0 in count[1:]: # 숫자가 없는 경우가 있는 경우 checker를 False로 반환하고 반복문 탈출
            checker = False
            break
    
    if checker:
        for c in range(9): # column에서 스도쿠 오류 있는지 탐색
            count = [0]*10
            for r in range(9):
                count[board[r][c]] += 1
            if 0 in count[1:]: # 숫자가 없는 경우가 있는 경우 checker를 False로 반환하고 반복문 탈출
                checker = False
                break
    
    if checker:
        for r in range(0,9,3):
            count = [0]*10
            for c in range(0,9,3):
                for dr, dc in d:
                    count[board[r+dr][c+dc]] += 1
                if 0 in count[1:]: # 숫자가 없는 경우가 있는 경우 checker를 False로 반환하고 반복문 탈출
                    checker = False
                    break
    
    checker = int(checker)
    print(f'#{tc} {checker}')
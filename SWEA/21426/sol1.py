T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int,input().strip().split())
    max_x = abs(x2-x1)+1
    max_y = abs(y2-y1)+1
    board = [[1]*max_x for _ in range(max_y)]
    find = False
    for _ in range(2):
        xa, ya, xb, yb = map(int, input().strip().split())
        for x in range(max(0,min(xa,xb)-min(x1,x2)), min(max_x,(max(xa,xb)-min(x1,x2) + 1))):
            for y in range(max(0,min(ya, yb)-min(y1,y2)), min(max_y,(max(ya, yb)-min(y1, y2) + 1))):
                board[y][x] = 0
    for x in range(max_x):
        for y in range(max_y):
            if board[y][x] == 1:
                print('YES')
                find = True
                break
        if find: break
    else: print('NO')
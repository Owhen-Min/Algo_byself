T = int(input())
for tc in range(T):
    inputs = input()
    dir = 0     # 0이 상단, 1이 우측, 2가 하단, 3이 좌측
    y, x = 0, 0
    max_y = [0]*2       # 최솟값, 최대값으로 이루어짐
    max_x = [0]*2
    deltas = (-1,0), (0, 1), (1,0), (0, -1)
    for move in inputs:
        if move == 'L':
            dir = (dir-1)%4
        elif move == 'R':
            dir = (dir+1)%4
        elif move == 'F':
            y += deltas[dir][0]
            x += deltas[dir][1]
            if y < max_y[0]:
                max_y[0] = y
            elif y > max_y[1]:
                max_y[1] = y
            elif x < max_x[0]:
                max_x[0] = x
            elif x > max_x[1]:
                max_x[1] = x
        else:
            y -= deltas[dir][0]
            x -= deltas[dir][1]
            if y < max_y[0]:
                max_y[0] = y
            elif y > max_y[1]:
                max_y[1] = y
            elif x < max_x[0]:
                max_x[0] = x
            elif x > max_x[1]:
                max_x[1] = x
    rec = (max_x[1]-max_x[0])*(max_y[1]-max_y[0])
    print(rec)
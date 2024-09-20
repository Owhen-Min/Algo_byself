T = int(input())
for tc in range(1,T+1):
    mat = [[0]*10 for _ in range(10)]
    trial = int(input())
    for t in range(trial):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if mat[i][j]== 0 or mat[i][j]== 2:
                        mat[i][j] += color

        else:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if mat[i][j]== 0 or mat[i][j]== 1:
                        mat[i][j] += color

        count = 0

        for i in range(10):
            for j in range(10):
                if mat[i][j] == 3:
                    count += 1

    print(f'#{tc} {count}')
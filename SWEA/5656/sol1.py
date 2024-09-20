def shoot(big_one, tries):
    mat, remains = *big_one
    for i in range(W):
        mat[i] = list(map(int, ''.join(map(str, mat[i])).replace('0', '').zfill(H)))
    # 정리하고

    if tries == 0 or remains == 0:
        global min_remains
        if min_remains > remains:
            min_remains = remains
        return
    # 끝났는지 확인하고

    for i in range(W):
        shoot(boom(mat, i),tries-1)
    # 쏘세요


def boom(matrix, row):
    for i in range(H):
        if matrix[row][i]:
            power = matrix[row][i]
            matrix[row][i] = 0
            break
    else: return
    blocks = set()
    for j in range(power-1,-power,-1):
        if 0 <= row+j < W:
            blocks.add((row+j, i, matrix[row+j][i]))
        if 0 <= i+j < H:
            blocks.add((row,i+j, matrix[row][i+j]))

    while blocks:
        blocks = chain(*blocks.pop(), blocks)
    remain = sum(1 for row in matrix for num in row if num > 0)

    return matrix, remain


def chain(i, j, power, blocks):
    matrix[i][j] = 0
    for k in range(power-1,-power,-1):
        if 0 <= i+k < W:
            blocks.add((i+k, j, matrix[i+k][j]))
        if 0 <= j+k < H:
            blocks.add((i,j+k, matrix[i][j+k]))
    return blocks


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(W)]
    mat_t = list(zip(*matrix))
    remains = sum(1 for row in mat_t for num in row if num > 0)
    min_remains = W*H
    shoot([mat_t, remains], N)
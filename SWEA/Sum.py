import sys
sys.stdin = open('sum_input.txt')

for tc in range(1,11):
    num = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    max_sum = -float('inf')
    # 행 합 검색
    for i in range(100):
        csum = 0
        for j in range(100):
            csum += mat[i][j]
        if max_sum<csum:
            max_sum = csum
    # 열 합 검색
    for j in range(100):
        rsum = 0
        for i in range(100):
            rsum += mat[i][j]
        if max_sum<rsum:
            max_sum = rsum
    # dsum1 = \, dsum2 = / 합 검색
    dsum1 = 0
    dsum2 = 0
    for i in range(100):
        dsum1 += mat[i][i]
        dsum2 += mat[i][99-i]
    if max_sum<dsum1:
        max_sum = dsum1

    if max_sum<dsum2:
        max_sum = dsum2

    print(f'#{num} {max_sum}')

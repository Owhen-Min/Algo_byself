T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    d = []
    for i in range(M):
        for j in range(M):
            d.append([i,j])
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            f_sum = 0
            for dx, dy in d:
                f_sum += flies[i+dx][j+dy]
            if max_sum < f_sum:
                max_sum = f_sum
    print(f'#{tc} {max_sum}')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    delta = [(1, 0), (0, 1)]
    max_len = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                for dy, dx in delta:
                    leng = 1
                    y = i
                    x = j
                    while y+dy<N and x+dx<M:
                        y += dy
                        x += dx
                        if matrix[y][x]: leng +=1
                        else: break
                    if max_len < leng: max_len = leng
    if max_len == 1: max_len = 0
    print(f'#{tc} {max_len}')

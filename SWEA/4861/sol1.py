T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    mat = [input() for _ in range(N)]
    ans = []
    for y in range(N):
        for x in range(N):
            for d in range(M):
                if x + d >= N or M+x-d-1 >= N or mat[y][x+d] != mat[y][M+x-d-1]:
                    break
            else:
                for d in range(M):
                    ans.append(mat[y][x+d])
            for d in range(M):
                if y + d >= N or M+y-d-1 >= N or mat[y+d][x] != mat[M+y-d-1][x]:
                    break
            else:
                for d in range(M):
                    ans.append(mat[y+d][x])

    print(f'#{tc} {"".join(ans)}')
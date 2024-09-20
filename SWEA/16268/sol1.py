T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    balloon = []
    for _ in range(N):
        balloon.append(list(map(int,input().split())))
    max_flower = 0
    delta = [[1,0],[-1,0],[0,1],[0,-1]]
    for x in range(M):
        for y in range(N):
            fl_sum = balloon[y][x]
            for k in range(4):
                dx, dy = delta[k]
                if 0<=x+dx<M and 0<=y+dy<N:
                    fl_sum += balloon[y+dy][x+dx]
            if max_flower < fl_sum:
                max_flower = fl_sum
    print(f'#{tc} {max_flower}')

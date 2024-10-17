deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    dir = dict()
    for i in range(N):
        ls = list(map(int,input().split()))
        for j in range(M):
            if ls[j]:
                dir[i,j] = (0, ls[j], ls[j]*2, ls[j])
                # 번식된 시간, 활성화되는 시간, 죽는 시간, 생명력
    t = 1
    while t <= K:
        acts = list(filter(lambda x: x[1][1] == t-1,list(dir.items())))
        for act in acts:
            y, x = act[0]
            for dy, dx in deltas:
                ny, nx = y+dy, x+dx
                if (ny, nx) in dir:
                    if dir[(ny, nx)][0] == act[1][0] and dir[(ny, nx)][3] < act[1][3]:
                        dir[(ny, nx)] = (t, t + act[1][3], t+ 2*act[1][3], act[1][3])
                else:
                    dir[(ny, nx)] = (t, t + act[1][3], t+ 2*act[1][3], act[1][3])
        t += 1
    print(f'#{tc} {sum(1 for x in dir.items() if x[1][2] > K)}')
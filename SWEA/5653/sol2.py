deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    dir = dict()

    # 좌표값 저장하기
    for i in range(N):
        ls = list(map(int, input().split()))
        for j in range(M):
            if ls[j]:
                # 딕셔너리 키 : 좌표 / 값 : 번식된 시간, 활성화되는 시간, 죽는 시간, 생명력
                dir[i, j] = (0, ls[j], ls[j] * 2, ls[j])

    t = 1
    while t <= K:
        # 갓 활성화된 세포들을 acts에 담는다. (좌표, 값들)의 형태들이 튜플의 형태로 모여 있다.
        acts = list(filter(lambda x: x[1][1] == t - 1, dir.items()))
        for act in acts:
            y, x = act[0]
            for dy, dx in deltas:
                ny, nx = y + dy, x + dx
                if (ny, nx) in dir:
                    # 새로 가려는 곳에 세포가 존재한다면, 세포가 시작된 시간이 자신과 같은지, 생명력이 더 큰지 비교한다.
                    if dir[(ny, nx)][0] == t and dir[(ny, nx)][3] < act[1][3]:
                        dir[(ny, nx)] = (t, t + act[1][3], t + 2 * act[1][3], act[1][3])
                else:
                    # 해당 장소에 기존에 세포가 없었다면, 덮어쓴다.
                    dir[(ny, nx)] = (t, t + act[1][3], t + 2 * act[1][3], act[1][3])
        t += 1

    # K만큼의 시간이 지난 후 살아있을 세포들
    count = sum(1 for x in dir.items() if x[1][2] > K)
    print(f'#{tc} {count}')

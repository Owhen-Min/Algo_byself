T = int(input())
d_h = [[0, 1], [0, 2], [0, 3], [0, 4]]
d_v = [[1, 0], [2, 0], [3, 0], [4, 0]]
d_d1 = [[1, 1], [2, 2], [3, 3], [4, 4]]
d_d2 =  [[-1, 1], [-2, 2], [-3, 3], [-4,4]]
deltas = [d_h, d_v, d_d1, d_d2]             # 하, 우, 대각선 델타 탐색할 deltas 할당.
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    finish = False                          # 값을 찾을 경우 True로 할당할 변수 설정
    for x in range(N):
        for y in range(N):
            if board[y][x] == 'o':          # 오목돌이 놓여져 있다면 델타 탐색 시작
                for delta in deltas:        # 방향에 따라서
                    for dx, dy in delta:    # dx, dy값을 받아와서
                        if 0 <= x + dx < N and 0 <= y + dy < N and board[y+dy][x+dx]== 'o':
                            pass            # 범위가 초과하지 않으면서 방향에 돌이 알맞게 놓여 있다면 그냥 넘어가고
                        else: break         # 잘 안됐다면 break로 멈춘다.
                    else:                   # 한번도 break가 걸리지 않았다면
                        finish = True       # finish를 True로 할당하고
                        print(f'#{tc} YES') # YES를 출력함.
                        break
            if finish: break
        if finish: break                    # 값을 이미 찾았다면 더 탐색할 필요가 없으니까 break
    else: print(f'#{tc} NO')                # 다 돌았는데 원하는 값을 못 찾았다면 NO를 print하고 다음 test case로 넘어간다.
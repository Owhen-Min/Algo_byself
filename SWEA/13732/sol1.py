T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    xys = []
    flag = False
    for i in range(N):
        for j in range(N):
            if board[i][j]=='#':
                xys.append((i, j))

    if int(len(xys)**.5)==len(xys)**.5:
        for y in range(int(len(xys)**.5)):
            for x in range(int(len(xys)**.5)):
                if ((y+xys[0][0]),(x+xys[0][1])) not in xys:
                    flag = True
                    print(f'#{tc} no')
                    break
            if flag: break
        else: print(f'#{tc} yes')
    else: print(f'#{tc} no')
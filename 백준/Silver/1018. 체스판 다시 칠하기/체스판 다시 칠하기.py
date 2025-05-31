def check_board(y, x):
    # 왼쪽 위가 흑으로 시작할 경우와 백으로 시작할 경우 다시 칠해야 하는 개수를 담을 변수 선언
    ls = [0,0]
    for k in range(8):
        for l in range(8):
            # 판이 흑일 때 뭐였어야 했는지 계산해서 변수에 추가
            if board[y+k][x+l] == 'B':
                if (k+l) %2:
                    ls[0] += 1
                else:
                    ls[1] += 1

            else:
                if (k+l) %2:
                    ls[1] += 1
                else:
                    ls[0] += 1
    return min(ls)


n, m = map(int,input().split())
board = [input() for _ in range(n)]
ans = 64
for i in range(n-8+1):
    for j in range(m-8+1):
        ans = min(ans, check_board(i, j))

print(ans)
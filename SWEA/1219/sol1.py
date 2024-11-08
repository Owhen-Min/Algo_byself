def DFS(s, e):
    stack = [0]*100
    stack[0] = s
    top = 0
    while top != -1:
        temp = stack[top]
        top -= 1
        if temp == 99:
            return 1
        for i in range(100):
            if board[temp][i] == 1:
                top += 1
                stack[top] = i
    return 0


for test_case in range(1, 11):
    tc, l = map(int, input().split())
    ls = list(map(int,input().split()))
    board = [[0] * 100 for _ in range(100)]
    for i in range (l):
        s, e = ls[2*i], ls[2*i+1]
        board[s][e] = 1
    print(f'#{tc} {DFS(0,99)}')

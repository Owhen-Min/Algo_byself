for test_case in range(1,11):
    tc = int(input())
    ladd = [list(map(int,input().split())) for _ in range(10)]
    y = 9
    dir = 0 # 방향이 0이면 위로, 1이면 왼쪽으로, 2면 오른쪽으로 이동 중임.
    delta = [[-1,1],-1,1] # dir index를 참조해서 대각선에 방향이 있는지 탐색

    for i in range (10):
        if ladd[y][i] == 2:
            x = i # 도착점 찾기. 거꾸로 올라갈 것임


    while y > 0:
        if dir == 0:
            for dx in delta[dir]:
                if 0 <= x+dx < 10 and ladd[y][x + dx]==1:
                    x += dx
                    dir = round((3+dx)/2)
                    y += 1
                    break
            y -= 1
        else:
            dx = delta[dir]
            if 0 <= x+dx < 10 and ladd[y-1][x+dx]==1:
                y -= 1
                x += dx
                dir = 0
            else: x += dx

    print(f'#{tc} {x}')
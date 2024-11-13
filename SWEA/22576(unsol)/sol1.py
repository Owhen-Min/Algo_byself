T = int(input())
for tc in range(T):
    a, b, c = map(int,input().split())
    if not a:
        # a가 0이라면 1차 방정식 또는 상수식
        if not b:
            # b도 0이라면, c가 0일 때 아무 수나 가능하므로 1을 출력
            if not c:
                print(1)
            # a와 b가 0인데 c가 0이 아니라면 어떤 수로도 불가능하므로 -1을 출력
            else:
                print(-1)
        else:
            # a가 0이고 b가 0이 아니라면, c가 0일 때 항상 x는 0이어야 하므로 0을 출력
            if not c:
                print(0)
            # b와 c가 0이 아니라면, x는 -c/b의 값을 가진다. 음수이므로 -1을 출력한다.
            else:
                print(-1)
        # 2차 방정식이라면
    else:
        # 판별식이 0 미만이라면 실수값이 존재하지 않으므로 -1 출력
        # 판별식이 0인 경우 항상 음수이므로 같이 -1로 출력
        if b**2 - 4*a*c <= 0:
            print(-1)
        # 판별식이 0이라면 
        else:
            if (-b + (b**2 - 4*a*c)**1/2)*2*a == int((-b + (b**2 - 4*a*c)**1/2)*2*a):
                print((-b + (b**2 - 4*a*c)**1/2)*2*a)
            else:
                print(-1)
            
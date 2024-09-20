def distrib(e=0,cnt=0):
    for i in range(e,24):           # 마지막에 끝난 시간으로부터 마지막까지
        if dict_trucks[i]:          # 요청서가 있다면
            distrib(dict_trucks[i][0],cnt+1)    # 그 작업이 끝나는 시간까지 작업을 한다고 침.
    global max_trucks
    if max_trucks < cnt:            # 지금까지의 cnt가 최대값이라면 걍산
        max_trucks = cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    dict_trucks= {}

    for i in range(0, 24):
        dict_trucks[i] = []                 # dict의 key에 0부터 23까지 넣어서 빈 리스트 생성.

    for i in range(N):
        s, e = map(int,input().split())
        dict_trucks[s].append(e)            # dict의 key는 시작시간, value는 끝나는 시간.

    for i in range (0, 24):
        dict_trucks[i].sort()               # dict value의 0번째 인덱스에 가장 빨리 끝나는 값이 오도록 sort

    max_trucks = 0
    distrib()
    print(f'#{tc} {max_trucks}')
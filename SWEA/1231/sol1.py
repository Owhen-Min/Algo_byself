def in_order(T):
    if (T):
        in_order(left[T])
        print(ls[T-1][1], end='')                       # 현재 위치의 글자를 프린트해주기 위해 인덱스 접근.
        in_order(right[T])

for tc in range(1, 11):
    N= int(input())
    ls = [list(input().split()) for _ in range(N)]      # 정점 번호 규칙과 글자를 한번에 받아준다.
    left = [0] * (N+1)
    right = [0] * (N+1)
    print(f'#{tc}', end=' ')

    for i in range(N//2-1):                 # N을 2로 나눈 몫의 -1동안 반복하면서 left와 right 노드를 더해준다. 왜 why? N이 짝수일 경우 마지막에 right가 없다.
        left[i+1] = int(ls[i][2])           # 리스트의 2번 인덱스를 left에 넣어준다.
        right[i+1] = int(ls[i][3])          # 리스트의 3번 인덱스를 right에 넣어준다.
    if N%2:                                 # 위에 밝힌 이유로 N이 짝수일 경우와 홀수일 경우를 나눠서 오류가 나지 않게 값을 더해준다.
        left[N//2] = int(ls[N//2-1][2])
        right[N//2] = int(ls[N//2-1][3])
    else: left[N//2] = int(ls[N//2-1][2])
    in_order(1)                             # 문제의 정의 상 1번이 루트이므로 1번에서 중위순회 시작
    print()                                 # 줄바꿈을 넣어준다.
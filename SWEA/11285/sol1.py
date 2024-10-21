T = int(input())

for tc in range (1, T+1):
    N = int(input())
    score = []
    darts = []
    for i in range(N):
        darts.append(list(map(int,input().split())))
    score = [11-(x**2+y**2)**1/2//20 for x, y in darts if (x**2+y**2)**1/2 < 11]
    print(f'#{tc} {sum(score)}')
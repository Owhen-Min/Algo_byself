def prod(level, made, cost):
    global min_cost
    # case 1. 현재까지의 cost가 최소 cost보다 큰 경우, 가지치기
    if min_cost < cost :
        return
    # case 2. 탐색을 다 끝냈을 경우, min_cost와 비교해서 더 작은 경우 갱신
    elif level == N:
        if min_cost > cost:
            min_cost = cost
    # case 3. 탐색을 다 끝내지 못한 경우, 못 가본 길에 대해 탐색한다.
    else:
        for i in range(N):
            if not made[i]:
                made[i] = 1
                prod(level+1, made, cost + costs[level][i])
                made[i] = 0

T = int(input())
for tc in range(1, T+1):
    N= int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 0
    for i in range(N):
        min_cost += costs[i][i]
    # 최소 비용의 초기값 : 대각선으로 모두 더한 값으로 설정.
    prod(0, [0]*N, 0)
    print(f'#{tc} {min_cost}')

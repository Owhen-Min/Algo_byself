def DFS(curr_y, curr_x, sum_til_now):
    global min_sum
    sum_til_now += matrix[curr_y][curr_x]       # 지금까지의 합에 현재 합을 더한다
    if sum_til_now > min_sum:                   # 만약 지금까지의 합이 최소 합보다 크면
        return                                  # 재귀함수 종료
    elif curr_x == curr_y==N-1:                 # 만약 끝까지 도달했다면
        if min_sum > sum_til_now:               # min_sum과 비교 후
            min_sum = sum_til_now               # 여태까지의 합이 더 작으면 갱신한다.
    else:
        if curr_x+1 < N: DFS(curr_y, curr_x+1, sum_til_now)
        if curr_y+1 < N: DFS(curr_y+1, curr_x, sum_til_now)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 2600
    DFS(0, 0, 0)
    print(f'#{tc} {min_sum}')
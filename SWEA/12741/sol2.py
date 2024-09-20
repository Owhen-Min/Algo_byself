T = int(input())
results = [0] * T
for tc in range(T):
    A, B, C, D = map(int,input().split())
    results[tc] = max(0,min(B,D)-max(A,C))
    # min(B,D) 더 먼저 꺼지는 전구 시간 - max(A,C) 더 늦게 켜지는 전구 시간
    # 만약 이게 겹치지 않는 경우 음수가 나오므로 0과 얘중 더 큰 애로 입력
for index, result in enumerate(results):
    print(f'#{index+1} {result}')

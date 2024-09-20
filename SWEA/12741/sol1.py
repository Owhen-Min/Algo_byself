T = int(input())
results = ''
for tc in range(T):
    A, B, C, D = map(int,input().split())
    results += f'#{tc+1} {max(0,min(B,D)-max(A,C))}\n'
    # min(B,D) 더 먼저 꺼지는 전구 시간 - max(A,C) 더 늦게 켜지는 전구 시간
    # 만약 이게 겹치지 않는 경우 음수가 나오므로 0과 얘중 더 큰 애로 입력
print(results[:-1])
# 매번 출력을 하면 시간이 초과하므로 결과를 하나의 문자열로 저장해서 한번에 출력한다.

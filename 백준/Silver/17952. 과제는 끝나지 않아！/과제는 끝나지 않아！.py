import sys
input = sys.stdin.readline

n = int(input())
stack = []  # 현재 하고 있는 과제만 관리
ans = 0     # 최종 점수

for _ in range(n):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        score, time = query[1], query[2]
        stack.append([score, time])  # 새로운 과제를 시작
    if stack:
        # 지금 하고 있는 과제 진행 (1분 소요)
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            # 과제 완료
            ans += stack[-1][0]
            stack.pop()

print(ans)

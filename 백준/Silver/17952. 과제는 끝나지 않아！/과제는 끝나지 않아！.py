import sys
input = sys.stdin.readline

N = int(input())  # 이번 학기 시간
score = 0  # 최종 결과 (이번학기에 받을 수 있는 총점
stack = []

# 이번 학기 시간동안 반복
for _ in range(N):
    info = list(map(int, input().split()))  # 

    # 과제 생기면 스택에 저장
    if info[0] == 1:
        a, t = info[1], info[2]
        stack.append([a, t])

    # 과제 하기
    if stack: # 스택이 비었을 수도 있으므로 체크
        stack[-1][1] -= 1 # 하던 과제를 해야지...(에휴)
        if stack[-1][1] == 0: # 과제 다했다면 점수 추가
            score += stack.pop()[0]

print(score)
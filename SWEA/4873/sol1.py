T = int(input())

for tc in range(1, T+1):
    s = input()
    stack = []
    top = -1
    for c in s:
        if top < 0:  # top이 음수라면, 즉 stack이 비어있다면 바로 추가
            stack.append(c)
            top += 1
        elif stack[top] == c:  # stack의 top, 마지막으로 추가된 값이 string 안의 character와 같다면
            stack.pop()  # stack의 마지막 값을 없애고, top을 -1 감소시킨다.
            top -= 1
        else:
            stack.append(c)  # stack의 top이 c와 같지 않다면, stack에 c를 추가하고, top 값도 증가시킨다.
            top += 1
    print(f'#{tc} {len(stack)}')  # stack에 쌓인 총 값을 출력한다.
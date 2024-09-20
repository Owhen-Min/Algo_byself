T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    top = -1
    dict = {
        '(' : None,
        ')' : '(',
        '{' : None,
        '}' : '{'
            }
    checker = True
    for c in string:
        if c in ['(','{']:  # 여는 괄호라면 스택에 추가
            stack.append(c)
            top += 1
        elif c in [')','}']:  # 닫는 괄호라면
            if top < 0:  # 스택이 비어 있을 경우
                checker = False
                break

            elif stack[top] == dict[c]:  # 스택의 마지막 괄호와 짝이 맞는다면
                stack.pop()
                top -= 1
            else:  # 스택의 마지막 괄호와 짝이 맞지 않는다면 0을 출력하고 탈출
                checker = False
                break
    if len(stack) != 0: checker = False
    if checker: print(f'#{tc} 1')  # 스택에 글자가 남아있지 않다면 1 출력
    else: print(f'#{tc} 0')  # 아니라면 0 출력
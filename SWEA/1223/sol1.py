def prefix_maker(arr):                  # 후위계산식 만드는 함수
    stack = []
    expression = []

    for c in arr:                       # arr의 글자를 하나씩 불러올 때
        if c in ['+','*']:              # 글자가 +나 *일 경우
            if stack:                   # stack이 비어있지 않으면
                if c == '*':            # 문자가 *일 경우
                    stack.append(c)     # stack에 *을 더한다.
                else:                   # 문자가 +일 경우
                    while stack:        # stack이 빌 때까지
                        expression.append(stack.pop())      # stack에 쌓여 있는 값을 표현식에 더한다.
                    stack.append(c)     # 그 후 +를 stack에 더한다.
            else: stack.append(c)       # stack이 비어있는 경우 글자를 stack에 더한다.
        else: expression.append(c)      # 글자가 숫자일 경우 표현식에 바로 더한다.
    while stack:                        # stack에 식이 남아 있는 경우
        expression.append(stack.pop())  # 표현식에 stack에 쌓여 있는 값들을 더한다.
    return expression                   # 표현식을 반환한다.


def prefix_cal(pf):                     # 후위계산식을 계산하는 함수
    stack = []
    for c in pf:                        # 후위계산식을 순회하면서
        if c not in ['+','*']:          # 글자가 숫자일 경우
            stack.append(c)             # 스택에 글자를 더한다.
        else:                           # 글자가 계산식일 경우
            if c == '+':                # 만약 +라면 두 수를 꺼내서 더한다.
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 + n1)
            elif c == '*':              # *라면 두 수를 꺼내서 곱한다.
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 * n1)
    return stack[0]                     # 스택에 쌓여있는 마지막 숫자를 토해낸다.


for tc in range(1, 11):
    N = int(input())
    arr = input()
    pf = prefix_maker(arr)
    print(f'#{tc} {prefix_cal(pf)}')
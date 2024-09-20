def postfix(ls):                                # 후위계산식으로 만드는 함수
    stack = []                                  # 스택과 표현식 생성
    expression = []
    for c in ls:
        if c == '+':                            # 글자가 + 일 경우
            for _ in range(len(stack)):         # stack에 쌓여있는 모든 연산자를 expression에 넣어놓고
                expression.append(stack.pop())
            stack.append(c)                     # stack에 연산자를 쌓는다.
        else: expression.append(c)              # 글자가 +가 아닐 경우 expression 에 쌓는다.
    else: expression = expression + stack       # for문이 다 끝나고 난 뒤 stack에 남아있을 연산자를 expression에 더해준다.

    return expression                           # 후위계산식으로 변환한 값을 리턴한다.

def cal_pf(ls):                                 # 후위 계산식을 계산하는 함수
    stack = []                                  # 빈 스택을 만든다.
    for c in ls:                                # ls 내내 글자들을 순회하면서
        if c != '+': stack.append(c)            # +가 아닐 경우, 즉 숫자일 경우 stack에 쌓는다.
        else:                                   # +일 경우
            n1 = int(stack.pop())               # stack의 제일 위에서 숫자를 뽑아 n1에 할당하고
            n2 = int(stack.pop())               # stack의 제일 위에서 한번 더 숫자를 뽑아 n2에 할당한 후
            stack.append(n1+n2)                 # 더한 숫자들을 stack에 append 해준다.
    return stack[0]                             # stack에 남은 계산값을 리턴한다.

for tc in range(1, 2):
    N = int(input())
    pf = postfix(input())
    print(f'#{tc} {cal_pf(pf)}')

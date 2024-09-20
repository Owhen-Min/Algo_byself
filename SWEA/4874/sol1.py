T = int(input())

for tc in range(1, T+1):
    ls = list(input().split())
    stack = []
    for char in ls:
        if char.isdigit():
            stack.append(char)
        else:
            if char == '.':
                if len(stack) == 1:
                    print(f'#{tc} {stack[0]}')
                else:
                    print(f'#{tc} error')
                break
            elif len(stack)>=2:
                if char == '+':
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())
                    stack.append(n2+n1)
                elif char == '-':
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())
                    stack.append(n2 - n1)
                elif char == '/':
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())
                    stack.append(n2 // n1)
                elif char == '*':
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())
                    stack.append(n2 * n1)
            else:
                print(f'#{tc} error')
                break


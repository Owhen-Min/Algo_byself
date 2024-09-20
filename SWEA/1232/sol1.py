def cal(index):
    if values[index].isdigit():     # index 위치의 node의 값이 숫자면
        return int(values[index])   # 숫자를 리턴한다
    else:
        if values[index] == '+':    # + 연산자라면 양 옆을 더한다
            return cal(left[index]) + cal(right[index])
        elif values[index] == '-':  # - 연산자라면 왼쪽에서 오른쪽을 빼준다
            return cal(left[index]) - cal(right[index])
        elif values[index] == '*':  # * 연산자라면 양 옆을 곱해준다
            return cal(left[index]) * cal(right[index])
        else: return cal(left[index]) / cal(right[index])   # / 연산자라면 왼쪽을 오른쪽으로 나눠준다


for tc in range(1, 11):
    N = int(input())
    left = [0] * (N+1)          # tree에서 왼쪽으로 뻗어갈 위치를 지정하는 right list
    right = [0] * (N+1)         # tree에서 오른쪽으로 뻗어갈 위치를 지정하는 right list
    values = [0] * (N+1)        # 노드의 값을 저장할 리스트 values

    for _ in range(N):       # 연산자와 노드 구조 받아오기
        i, value, *ls  = input().split()        # 연산자는 문자열로 처리해야하므로 map 함수를 쓰지 않는다.
        values[int(i)]= value
        if ls:
            left[int(i)] = int(ls[0])
            right[int(i)] = int(ls[1])
    print(f'#{tc} {int(cal(1))}')               # 연산은 실수로 진행하나 출력값은 정수로 해야 하므로 int() 함수로 감싸준다.
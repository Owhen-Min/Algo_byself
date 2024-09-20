T = int(input())
for tc in range(1, T+1):
    irons = input().replace('()','*')   # 쇠막대기 input 받기. 레이저'()'는 *로 변환하여 받음
    stack_num = cnt = 0                 # stack에 들어갈 글자가 '('밖에 없고, 길이만 중요하므로 숫자로 카운트. 총 개수를 셀 cnt도 선언.
    for iron in irons:                  # 글자를 순회하면서
        if iron == '(':                 # 쇠막대기가 시작한다면
            stack_num +=1               # 스택에 1을 더하고
            cnt +=1                     # 총 개수에도 1을 더한다.
        elif iron == '*':               # 레이저일 경우
            cnt += stack_num            # 현재 진행되고 있는 쇠막대기 만큼 갯수를 더한다.
        else:                           # ')' 가 나와서 쇠막대기가 끝난다면
            stack_num -= 1              # 스택에 1을 빼준다.
    print(f'#{tc} {cnt}')               # 총 카운트를 센다.
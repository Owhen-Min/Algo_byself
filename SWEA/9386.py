T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = list(map(int,(input())))
    max_len = 0
    length = 0
    ls = []

    for i in range (N):
        if s[i]:
            length += 1 # 1일 경우 length에 1 더하기
        else:
            ls.append(length) # 0일 경우 length에 지금까지 더해진 값 ls에 저장
            length = 0
    if length != 0:
        ls.append(length) # 마지막이 1이었을 경우 length의 값을 별도로 저장해줌.

    for item in ls: # ls의 최댓값 구하기
        if max_len < item:
            max_len = item
    print(f'#{tc} {max_len}')
T= int(input())
p_tri = [[1]]                   # 첫째 줄은 1만
for tc in range(1, T+1):
    print(f'#{tc}')             # 인덱스를 미리 밝혀준다.
    N = int(input())            # 원하는 길이를 N으로 받는다.
    if N <= len(p_tri):         # 이미 p_tri에 입력해둔 값보다 N이 작다면
        for i in range(N):
            print(*p_tri[i])    # N번 줄까지 p_tri를 출력한다.
    else:
        for i in range(len(p_tri),N):   # 현재 길이부터 원하는 길이 N까지 반복한다.
            ls = [1]                    # 추가할 줄의 제일 왼쪽 칸은 무조건 1이고,
            for j in range(i-1):        # 그 뒤부터는 윗칸의 자신의 인덱스와 자신의 인덱스 + 1 칸의 합을 할당해서 리스트에 추가한다.
                ls.append(p_tri[i-1][j]+p_tri[i-1][j+1])
            ls.append(1)                # 리스트의 제일 마지막은 무조건 1이다.

            p_tri.append(ls)            # 이렇게 생성한 값을 p_tri에 추가한다.

        for i in range(N):
            print(*p_tri[i])
T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split()) # 전체 페이지 P, a의 타겟 Pa, b의 타겟 Pb
    ca = cb = 0 # 동시 비교를 위해 A와 B의 중간인 변수
    la = lb = 1 # 검색 구간의 왼쪽 시작
    ra = rb = P # 검색 구간의 오른쪽 시작

    while ca != Pa and cb != Pb:
        ca = int((la + ra)/2)
        cb = int((lb + rb) / 2)

        if ca < Pa: la = ca
        else: ra = ca

        if cb < Pb: lb = cb
        else: rb = cb

    if ca == Pa: # 반복이 끝나고 a가 목표 번호에 도달했을 때
        if cb == Pb: # b도 목표 번호에 도달했다면 무승부
            result = 0
        else: result = 'A' # 아니면 a가 이겼다
    else: result = 'B' # 반복이 끝나고 b만 목표 번호에 도달했다면 B가 이겼다.

    print(f'#{tc} {result}')

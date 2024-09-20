for _ in range(1, 11):
    tc = input()
    matt = [input() for _ in range(100)]
    ans = 1 # 회문이 없을 경우 제출할 최소길이값 1
    for leng in range (100, -1, -1): # 가장 길이가 긴 회문부터 탐색 후 for문 종료
        if ans != 1: break # 정답을 찾았을 경우, for문을 나온다. 이하 동문
        for x in range (0, 100):
            if ans != 1: break
            for y in range(0, 100):
                if ans != 1: break
                for d in range(leng//2): # x좌표 + 목표 길이가 전체보다 길 경우 or 회문이 아닐 경우 탐색 종료
                    if x+leng >= 101 or matt[y][x+d] != matt[y][leng+x-d-1]:
                        break
                else: ans = leng # 탐색을 모두 했어도 오류가 없다면, 찾은 회문의 길이를 정답에 저장

                for d in range(leng//2): # y좌표 + 목표 길이가 전체보다 길 경우 or 회문이 아닐 경우 탐색 종료
                    if y+leng >= 101 or matt[y+d][x] != matt[leng+y-d-1][x]:
                        break
                else: ans = leng

    print(f'#{tc} {ans}')

T = int(input())
for tc in range (1, T+1):
    s1 = input()
    s2 = input()
    for i in range(len(s2)-len(s1)+1):
        checker = False
        if s2[i] == s1[0]: # 만약에 s2의 i 번째 열이 s1의 첫 번째 열과 같으면
            checker = True # 일단 checker을 True로 반환하고
            for j in range(1,len(s1)): # s1의 나머지 열이 이어지는 열들 중 같지 않은 경우
                if s2[i+j] != s1[j]: checker = False # checker를 False로 바꾼다

        if checker: # checker가 True라면 1을 출력하고 반복문을 종료한다.
            print(f'#{tc} 1')
            break
    if not checker: print(f'#{tc} 0') # 다 돌 동안 checker가 True가 아니라면 0을 출력한다.
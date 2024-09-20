T = int(input())
for tc in range(1, T+1):
    cards = list(map(int,input().split()))
    p1 = []
    p2 = []
    result = 0
    for i in range(6):
        p1.append(cards[2*i])
        p2.append(cards[2*i+1])
        p1.sort()
        p2.sort()
        
        # p1 검사
        for j in range(len(set(p1))-2):
            if list(set(p1))[j]+2 == list(set(p1))[j+1]+1 == list(set(p1))[j+2]:
                result = 1
                break
        for j in range(i - 1):
            if p1[j] == p1[j+1] == p1[j+2]:
                result = 1
                break
        if result: break
        
        # p2 검사
        ls = list(set(p2))
        for j in range(len(set(p2)) - 2):
            if ls[j] + 2 == ls[j + 1] + 1 == ls[j + 2]:
                result = 2
                break

        for j in range(i-1):
            if p2[j] == p2[j+1] == p2[j+2]:
                result = 2
                break
        if result: break

    print(f'#{tc} {result}')
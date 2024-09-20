T = int(input())
for tc in range(1, T+1):
    size = int(input())
    ls = list(map(int,input().split()))
    for i in range(len(ls)-1):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]

    print(f'#{tc} {ls[-1]-ls[0]}')
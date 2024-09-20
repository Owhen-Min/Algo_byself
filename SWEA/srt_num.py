T = int(input())
for tc in range (1,T+1):
    N = int(input())
    ls = list(map(int,input().split()))
    for i in range(N):
        for j in range(N-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    print(f'#{tc}', end= ' ')
    for num in ls:
        print(num, end= ' ')
    print()
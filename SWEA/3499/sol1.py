T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ls = list(input().split())
    print(f'#{tc}', end=' ')
    if N%2:
        for i in range(N//2):
            print(ls[i], ls[(N//2)+1+i], end=' ')
        print(ls[N//2])
    else:
        for i in range(N // 2):
            print(ls[i], ls[(N//2) + i], end=' ')
        print()

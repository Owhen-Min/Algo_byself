T= int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    s = ''
    while M != 0:
        if M%2: s = '1' + s
        else: s = '0' + s
        M //= 2
    if s[-N:] == '1'*N: print(f'#{tc} ON')
    else: print(f'#{tc} OFF')
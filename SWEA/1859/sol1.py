T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ls = list(map(int,input().split()))
    hap = 0
    l_num = ls[n-1]
    for item in ls[::-1]:
        if l_num < item:
            l_num = item
        else:
            hap += l_num-item
    print(f'#{tc} {hap}')

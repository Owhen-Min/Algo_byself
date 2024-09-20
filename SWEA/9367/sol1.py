T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int,input().split()))
    temp = 1
    max_leng = 1
    for i in range(N-1):
        if ls[i]<ls[i+1]: temp += 1
        else:
            if max_leng < temp: max_leng = temp
            temp = 1
    if max_leng < temp: max_leng = temp
    print(f'#{tc} {max_leng}')

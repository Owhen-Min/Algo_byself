for tc in range(1, 11):
    length = int(input())
    ls = list(map(int,input().split()))
    view = 0
    for i in range(2, length-2):
        if ls[i] == max(ls[i-2:i+3]):
            difference = ls[i]-max([ls[i-2],ls[i-1], ls[i+1], ls[i+2]])
            view += difference
    print(f'#{tc} {view}')

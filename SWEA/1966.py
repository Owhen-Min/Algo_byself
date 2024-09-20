T = int(input())
for tc in range(1, T+1):
    l = int(input())
    ls = list(map(int,input().split()))
    for i in range (l-1):
        min_index = i
        for j in range(i+1, l):
            if ls[min_index] > ls[j]:
                min_index = j
        ls[i], ls[min_index] = ls[min_index], ls[i]
    print(f'#{tc}', *ls)


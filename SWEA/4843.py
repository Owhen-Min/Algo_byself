T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int,input().split()))
    for i in range(0,N,2):
        max_index = i
        for j in range(i, N):
            if ls[max_index] < ls[j]:
                max_index = j
        ls[max_index], ls[i] = ls[i], ls[max_index]
        min_index = i+1
        for j in range(i+1, N):
            if ls[min_index] > ls[j]:
                min_index = j
        ls[min_index], ls[i+1] = ls[i+1], ls[min_index]
    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(ls[i], end= ' ')
    print()

    # for i in range(0,N,2):
    #     max_num = ls[i]
    #     min_num = ls[i]
    #     max_index = i
    #     min_index = i
    #     for j in range(i,lN):
    #         if max_num < ls[j]:
    #             max_index = j
    #             max_num = ls[j]
    #         if min_num > ls[j]:
    #             min_index = j
    #             min_num = ls[j]
    #     ls[max_index], ls[min_index], ls[i], ls[i+1] = ls[i], ls[i+1], ls[max_index], ls[min_index]
    # print(f'#{tc}', end = ' ')
    # print(*ls)



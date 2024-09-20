T = int(input())

for tc in range(1,T+1):
    ls = list(map(int,input().split()))
    subsets = [[]]
    for item in ls:
        size = len(subsets)
        for i in range(size):
            subsets.append(subsets[i]+[item])

    checker = 0
    for subset in subsets[1:]:
        s_sum = 0
        for item in subset:
            s_sum += item
        if s_sum == 0:
            checker = 1

    print(f'#{tc} {checker}')

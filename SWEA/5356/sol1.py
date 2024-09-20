T = int(input())

for tc in range(1, T+1):
    ls = []
    for _ in range(5):
        ls.append(list(input()))

    max_len = 0
    for i in range(5):
        if max_len<len(ls[i]): max_len = len(ls[i])

    nls = []
    for _ in range(max_len):
        nls.append(['']*5)

    for i in range(5):
        for j in range(len(ls[i])):
            nls[j][i] = ls[i][j]

    print(f'#{tc}',end=' ')
    for lis in nls:
        for item in lis:
            print(item, end='')
    print()
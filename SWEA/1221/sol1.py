T = int(input())
dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
r_ls = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    dump, cases = input().split()
    cases = int(cases)
    ls = input().split()
    nls = [0]*cases
    for i in range(cases):
        nls[i] = dic[ls[i]]

    for i in range(len(ls)-1):
        for j in range(len(ls)-i-1):
            if nls[j] > nls[j+1]:
                nls[j], nls[j+1] = nls[j+1], nls[j]

    for i in range(cases):
        ls[i] = r_ls[nls[i]]

    print(f'#{tc}')
    print(*ls)
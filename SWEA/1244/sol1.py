T = int(input())
for tc in range(1, T+1):
    ls, N = input().split()
    N = int(N)
    ls = list(map(int,ls))
    i= 0
    j= 0

    if len(ls) == 1:
        print(f'#{tc}',*ls)

    while i < N:
        if j != N:
            max_num = ls[j]
            max_index = j
            for k in range(1, len(ls)-j):
                if max_num <= ls[j+k]:
                    max_num = ls[j+k]
                    max_index = j+k

            if max_index != j:
                ls[j], ls[max_index] = ls[max_index], ls[j]
                i += 1
                j += 1
            else:
                j += 1
        else:
            ls = map(str,ls)
            if len(set(ls))!=len(ls):
                print(f'#{tc} {"".join(ls)}')
                break
            else:
                if (N-i)%2:
                    ls[-1], ls[-2] = ls[-2], ls[-1]
                    print(f'#{tc} {"".join(ls)}')
                    break
                else:
                    print(f'#{tc} {"".join(ls)}')
                    break
    else:
        ls = map(str,ls)
        print(f'#{tc} {"".join(ls)}')
for tc in range(1, int(input())+1):
    n1, n2 = map(int, input().split())
    s1 = set()
    s2 = set()
    ans = set()
    for _ in range(n1):
        s1.add(input())
    for _ in range(n2):
        s2.add(input())
    for elem in s2:
        if elem in s1:
            ans.add(elem)
    ans = list(sorted(ans))
    # if ans:
    #     print(f'#{tc} {*ans}')
    # else: print(f'#{tc} NO!!')
    print(*ans)
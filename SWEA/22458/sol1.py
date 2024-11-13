for tc in range(1, int(input())+1):
    n1, n2 = map(int, input().split())
    s1 = ''
    s2 = ''
    for i in range(n1):
        s1 += input()+' '
    for i in range(n2):
        s2 += input()+' '
    print(s1, s2)
    s1 = set(s1.split())
    s2 = set(s2.split())
    ans = sorted(s1&s2)
    if ans:
        print(f'#{tc}', *ans)
    else: print(f'#{tc} NO!!')

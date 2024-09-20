T = int(input())
for tc in range(1, T+1):
    s1 = set(input())
    s2 = input()
    ct = {}
    for s in s2:
        if s in s1:
            if s in ct:
                ct[s] += 1
            else: ct[s] = 1
    print(f'#{tc} {max(ct.values())}')
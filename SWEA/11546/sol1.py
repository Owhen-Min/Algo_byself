from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people = deque()
    As, Bs, Cs = set(), set(), set()
    for _ in range(N):
        A, B, C = map(int,input().split())
        As.add(A)
        Bs.add(B)
        Cs.add(C)
        people.append((A, B, C))

    poss_comb = deque()
    for A in As:
        for B in Bs:
            if A + B <= 10000:
                try: poss_comb.append((A,B,max(C for C in Cs if C <= 10000-A-B)))
                except: continue

    max_num = 0
    for comb in poss_comb:
        num=0
        for person in people:
            if comb[0] >= person[0] and comb[1] >= person[1] and comb[2] >= person[2]:
                num += 1
        if max_num < num:
            max_num = num

    print(f'#{tc} {max_num}')



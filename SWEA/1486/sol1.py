def tower(out, S, min_diff=100000, last = 0):
    if S < B:
        return min_diff
    else:
        diff = S - B
        if min_diff > diff:
            min_diff = diff
        for i in range(last, N):
            if not out[i]:
                out[i] = 1
                min_diff = tower(out, S - clerks[i], min_diff, i)
                out[i] = 0
        return min_diff


T = int(input())
for tc in range(1, T+1):
    N, B = map(int,input().split())
    clerks = list(map(int,input().split()))
    S = sum(clerks)
    print(f'#{tc} {tower([0]*N, S)}')
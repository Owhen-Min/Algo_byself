def bt(parent):
    if parent:
        global values, k
        bt(left[parent])
        values[parent] = k
        k += 1
        bt(right[parent])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    i = 1
    j = 1
    left = [0] * (N+1)
    right = [0] * (N+1)
    while i <= N:
        if i == 1:
            i += 1
            continue
        if i+1 > N:
            left[j] = i
        else:
            left[j] = i
            right[j] = i+1
        i += 2
        j += 1
    values = [0] * (N+1)
    k = 1
    bt(1)
    print(f'#{tc}', values[1], values[N//2])

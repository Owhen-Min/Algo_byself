from collections import deque


T = int(input())
for tc in range(1, T+1):
    n, k = map(int,input().split())
    planets = sorted(list(map(int,input().split())))
    tries = 0
    dq = deque()
    i = 0

    while i < n:
        if k >= planets[i]:
            dq.append(planets[i])
            i += 1
        elif dq:
            k += dq.pop()
            tries += 1
        else:
            tries = -1
            break
    total = sum(dq)
    while dq:
        last = dq.pop()
        if total > k:
            k += last
            total -= last
            tries += 1
    print(f'#{tc} {tries}')

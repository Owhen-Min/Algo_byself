from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    planets = sorted(list(map(int, input().split())))
    tries = 0
    dq = deque()
    i = 0

    while i < len(planets):
        if k >= planets[i]:
            dq.append(planets[i])
            i += 1
        elif dq:
            k += dq.pop()
            tries += 1
        else:
            tries = -1
            break
    while dq:
        if dq[-1] <= k:
            last = dq.pop()
            k -= last
        else:
            k += last * 2
            tries += 1
    print(f'#{tc} {tries}')
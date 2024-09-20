import heapq

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    planets = sorted(map(int, input().split()))
    tries = 0
    conquered = []

    for planet in planets:
        while k < planet:
            if not conquered:
                tries = -1
                break
            mobilized = -heapq.heappop(conquered)
            k += mobilized
            tries += 1

        if tries == -1:
            break

        k -= planet
        heapq.heappush(conquered, -planet)

    print(f'#{tc} {tries})
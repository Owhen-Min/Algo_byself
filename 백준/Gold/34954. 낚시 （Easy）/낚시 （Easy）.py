import heapq
n, m = map(int,input().split())
baits = list(map(lambda x: -x, map(int,input().split())))
fish = list(map(lambda x: -x, map(int,input().split())))
heapq.heapify(baits)
heapq.heapify(fish)

ans = 0

while baits and fish:
    curr_fish = heapq.heappop(fish)

    while baits:
        curr_bait = heapq.heappop(baits)
        if curr_bait > curr_fish:
            ans -= curr_fish
            break

print(ans)
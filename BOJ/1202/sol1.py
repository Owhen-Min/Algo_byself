import heapq


n, k = map(int,input().split())
gems = [list(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()
hap = 0

gem_index = 0
poss_gems = []
for bag in bags:
    while gem_index < n:
        if bag >= gems[gem_index][0]:
            heapq.heappush(poss_gems, -gems[gem_index][1])
            gem_index += 1
        else: break
    if poss_gems:
        hap -= heapq.heappop(poss_gems)

print(hap)
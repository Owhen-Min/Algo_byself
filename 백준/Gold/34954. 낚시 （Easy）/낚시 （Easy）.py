import heapq

n, m = map(int,input().split())
baits = sorted(map(int,input().split()))
fish = sorted(f for f in map(int,input().split()) if f > baits[0])
m = len(fish)

i = j = 0
ans = 0
caught = []

while j<m:
    # 떡밥으로 물고기를 잡을 수 있을 때 > 무조건 잡는디!
    if i<n and baits[i] < fish[j]:
        heapq.heappush(caught, fish[j])
        ans += fish[j]
        i += 1
        j += 1
    # 떡밥으로 물고기를 잡을 수 없을 때
    else:
        # 기존에 물고기 잡아둔게 있다면 물고기로 떡밥을 만들어서 새로운 물고기를 잡는다
        if caught:
            ans += fish[j] - heapq.heappop(caught)
            heapq.heappush(caught, fish[j])
        j += 1

print(ans)

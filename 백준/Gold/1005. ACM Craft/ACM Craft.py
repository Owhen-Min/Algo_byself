from collections import defaultdict
from heapq import heappush, heappop, heapify


def finishing_node(node):
    for nxt in orders[node]:
        buildings[nxt] -= 1
        if buildings[nxt] == 0:
            heappush(inbuild, [times[nxt], nxt])


for _ in range(int(input())):
    n, k = map(int,input().split())
    # 위상정렬을 위한 빈 리스트 buildings
    buildings = [0]*n

    # 건물을 짓는 데 드는 시간을 담을 변수 times
    times = tuple(map(int,input().split()))

    # 건물이 완성되고 나서 제약사항을 확인할 dict orders
    orders = defaultdict(list)

    for __ in range(k):
        x, y = map(int,input().split())
        orders[x-1].append(y-1)
        buildings[y-1] += 1

    target = int(input()) -1

    ans = 0

    # 현재 지어지고 있는 건물의 리스트를 담을 inbuild
    inbuild = [[times[index], index] for index, enter in enumerate(buildings) if enter == 0]

    # 가장 시간이 적게 드는 애 기준으로 나머지 애들의 시간을 줄여줄거니까 heap 구조로 만듦.
    heapify(inbuild)

    while True:
        build_time, curr = heappop(inbuild)

        ans += build_time
        if curr == target:
            break

        if build_time:
            inbuild = list(map(lambda x: [x[0] - build_time, x[1]], inbuild))

        for nxt in orders[curr]:
            buildings[nxt] -= 1
            if buildings[nxt] == 0:
                heappush(inbuild, [times[nxt], nxt])


    print(ans)
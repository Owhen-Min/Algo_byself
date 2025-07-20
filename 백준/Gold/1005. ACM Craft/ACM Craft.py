from collections import defaultdict
from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, k = map(int, input().split())
    # 위상정렬을 위한 빈 리스트 buildings
    buildings = [0] * n

    # 건물을 짓는 데 드는 시간을 담을 변수 times
    times = tuple(map(int, input().split()))

    # 건물이 완성되고 나서 제약사항을 확인할 dict orders
    orders = defaultdict(list)

    for __ in range(k):
        x, y = map(int, input().split())
        orders[x - 1].append(y - 1)
        buildings[y - 1] += 1

    target = int(input()) - 1

    # 현재 시간
    current_time = 0

    # 현재 지을 수 있는 건물들 (시간, 건물 인덱스)
    inbuild = [(times[index], index) for index, enter in enumerate(buildings) if enter == 0]
    heapify(inbuild)

    while inbuild:
        build_time, curr = heappop(inbuild)

        current_time = build_time

        if curr == target:
            break

        # 다음에 지을 수 있는 건물들 추가
        for nxt in orders[curr]:
            buildings[nxt] -= 1
            if buildings[nxt] == 0:
                heappush(inbuild, (current_time + times[nxt], nxt))

    print(current_time)
import sys
input = sys.stdin.readline

from heapq import heappush, heappop
from collections import defaultdict

t = int(input())
for _ in range(t):
    k = int(input())
    count = defaultdict(int)
    max_h = []
    min_h = []

    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":
            heappush(max_h, -num)
            heappush(min_h, num)
            count[num] += 1
        else:
            try:
                if num == 1:
                    curr = -heappop(max_h)
                    while count[curr] == 0:
                        curr = -heappop(max_h)
                    count[curr] -= 1
                else:
                    curr = heappop(min_h)
                    while count[curr] == 0:
                        curr = heappop(min_h)
                    count[curr] -= 1
            except IndexError:
                pass
    try:
        while count[-max_h[0]] == 0:
            heappop(max_h)
        while count[min_h[0]] == 0:
            heappop(min_h)
    except IndexError:
        pass

    if max_h:
        print(f"{-heappop(max_h)} {heappop(min_h)}")
    else:
        print("EMPTY")

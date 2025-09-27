import sys
from itertools import accumulate
input = sys.stdin.readline

n = int(input())
dists = list(accumulate((int(input()) for _ in range(n))))

ans = 0

i, j = 0, 1

w_dist = dists[-1]

while j < n:
    clockwise = dists[j]-dists[i]
    counter_clockwise = w_dist - clockwise
    if counter_clockwise > clockwise:
        j += 1
        ans = max(ans, clockwise)
    else:
        i += 1
        ans = max(ans, counter_clockwise)

print(ans)
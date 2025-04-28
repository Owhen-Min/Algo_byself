# 뒤에서부터 생각하기.
# 뒤에 남은 시간보다 이번에 맞닥뜨린 일이 더 길다면, 새로운 일을 만나기 전까지는 아무런 진전이 없을 것임.
# 따라서 일을 가지고 남은 시간을 생각하면서 뒤에서부터 하나하나 풀 수 있는 과제인지, 못 푸는 과제인지 따지기.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
stack = deque()
ans = 0

for i in range(n):
    index, *info = map(int, input().split())
    if info:
        stack.append((i, info))

last = n

while stack:
    time, (score, burden) = stack.pop()
    if last >= burden + time:
        ans += score
        last -= burden
    else:
        last = time

print(ans)
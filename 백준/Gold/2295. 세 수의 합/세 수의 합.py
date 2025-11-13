import sys
input = sys.stdin.readline
from itertools import product

n = int(input())
nums = sorted(int(input()) for _ in range(n))

sums = set(sum(elems) for elems in product(nums, repeat =2))

for i in range(n-1, -1, -1):
    curr = nums[i]
    for j in range(i):
        if curr - nums[j] in sums:
            ans = curr
            break
    else:
        continue
    break

print(ans)
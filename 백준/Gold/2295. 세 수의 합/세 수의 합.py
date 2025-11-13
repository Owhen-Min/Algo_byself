import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

n = int(input())
nums = sorted(int(input()) for _ in range(n))

sums = set(n1+n2 for n1, n2 in combinations_with_replacement(nums, 2))

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
from itertools import combinations
from collections import Counter

n, s = map(int,input().split())
nums = list(map(int,input().split()))
left, right = Counter(), Counter()
for i in range(n//2+1):
    left.update(map(sum, combinations(nums[:n//2], i)))
    right.update(map(sum, combinations(nums[n//2:], i)))
if n%2:
    right[sum(nums[n//2:])]+=1

l_keys = sorted(left.keys())
r_keys = sorted(right.keys(), reverse=True)

li, ri = 0, 0

# 원하는 합이 0인 경우 양측 집단에서 아무것도 고르지 않은 경우를 제외.
if s == 0:
    ans = -1
else:
    ans = 0

while ri < len(r_keys) and li < len(l_keys):
    curr = l_keys[li] + r_keys[ri]
    if curr > s:
        ri += 1
    else:
        if curr == s:
            ans += left[l_keys[li]]*right[r_keys[ri]]
        li += 1

print(ans)
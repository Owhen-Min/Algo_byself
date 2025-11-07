n = int(input())
nums = sorted(map(int,input().split()))

ans = 0

for i in range(n):
    left, right = 0, n-1
    target = nums[i]
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                ans += 1
                break
        else:
            if curr < target: left += 1
            else: right -= 1

print(ans)

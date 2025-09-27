n, m = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = max(arr)-min(arr)

def can_divide(target, max_tries):
    cnt = 1
    min_sec = max_sec = arr[0]

    for i in range(n):
        min_sec = min(arr[i], min_sec)
        max_sec = max(arr[i], max_sec)
        if max_sec - min_sec > target:
            min_sec = max_sec = arr[i]
            cnt += 1

    return cnt <= max_tries

while left <= right:
    mid = (left+right)//2
    if can_divide(mid, m):
        right = mid-1
    else:
        left = mid+1

print(left)
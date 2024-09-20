def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        global left_big
        left_big += 1

    return merge(left, right)


def merge(left, right):
    result = [0] * (len(left)+len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mid_big = 0
    left_big = 0
    print(f'#{tc}', merge_sort(arr)[N//2], left_big)
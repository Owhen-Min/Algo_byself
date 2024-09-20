T = int(input())
for tc in range(1, T+1):
    size = int(input())
    arr = list(map(int, input().split()))
    ls = [0]*(size-1)
    for i in range(size-1):
        ls[i] = size - arr.index(arr[i]) - 1 - len([x for x in arr if x >= arr[i]])
    print(f'#{tc} {max(ls)}')

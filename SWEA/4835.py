T = int(input())
for tc in range(1, T + 1):
    size, hap = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = sum(arr[0:hap])
    min_sum = sum(arr[0:hap])
    for i in range(size-hap+1):
        if sum(arr[i:i+hap])>max_sum:
            max_sum = sum(arr[i:i+hap])
        elif sum(arr[i:i+hap])<min_sum:
            min_sum = sum(arr[i:i+hap])
    print(f'#{tc} {max_sum-min_sum}')


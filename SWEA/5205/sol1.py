def hoare_partition(left, right):
    mid = (left+right)//2
    pivot = ls[mid]
    ls[left], ls[mid] = ls[mid], ls[left]
    i = left +1
    j = right
    while i <= j:
        while i <= j and ls[i] <= pivot:
            i += 1
        while i <= j and ls[j] >= pivot:
            j -= 1
        if i < j:
            ls[i], ls[j] = ls[j], ls[i]

    ls[left], ls[j] = ls[j], ls[left]

    return j


def quick_sort(l, r):
    if l < r:
        pivot = hoare_partition(l, r)
        quick_sort(l, pivot-1)
        quick_sort(pivot+ 1, r)


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int,input().split()))
    quick_sort(0,N-1)
    print(f'#{tc} {ls[N//2]}')
def subtree(num, i):
    if num == 0:
        return i
    else: return subtree(left[num], i+1) + subtree(right[num], 0)

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    ls = list(map(int,input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    for i in range(E):
        if left[ls[2*i]]:
            right[ls[2*i]] = ls[2*i+1]
        else: left[ls[2*i]] = ls[2*i+1]
    print(f'#{tc} {subtree(N, 0)}')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hip = [0] * (N+1)
    ls = list(map(int,input().split()))
    last = 0
    for num in ls:
        last +=1
        hip[last] = num
        temp = last
        while temp > 1:
            if hip[temp] < hip[temp//2]:
                hip[temp//2], hip[temp] = hip[temp], hip[temp//2]
                temp //= 2
            else: break
    anc_sum = 0
    while N >= 1:
        anc_sum += hip[N//2]
        N //= 2
    print(f'#{tc} {anc_sum}')

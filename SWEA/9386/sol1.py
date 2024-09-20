T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = input()
    temp = 0
    max_len = 0
    for i in range(N):
        if ls[i] == '1': temp += 1
        else:
            if max_len < temp : max_len = temp
            temp = 0
    if max_len < temp: max_len = temp
    print(f'#{tc} {max_len}')
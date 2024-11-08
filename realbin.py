T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    for _ in range(n):
        next_num, res = divmod(m,2)
        if not res:
            print(f'#{tc} OFF')
            break
        m = next_num
    else:
        print(f'#{tc} ON')
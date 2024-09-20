T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = input().split('0')
    print(f'#{tc} {len(max(ls))}')
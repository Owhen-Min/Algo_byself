def p_game(N):
    if N == 10: return 1
    elif N == 20: return 3
    else: return p_game(N-10)+p_game(N-20) * 2

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {p_game(int(input()))}')
T = int(input())
cases = []
max_N = 0
for _ in range(T):
    N = int(input())
    cases.append(N)
    if N > max_N: max_N = N

reduced = list(range(max_N+1))

for i in range (2, int(max_N**0.5)+1):
    i_square = i**2
    for j in range (i_square, max_N+1, i_square):
        while reduced[j] % i_square == 0:
            reduced[j] //= i_square

results = []

for tc in range(1, T+1):
    print(f'#{tc} {reduced[cases[tc-1]]}')
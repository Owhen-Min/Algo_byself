T = int(input())
ls = [0] * T
for i in range(T):
    ls[i] = int(input())
max_num = max(ls)
squares = [0] + list(range(1, max_num+1))
for i in range(int((max_num+1)**.5),1,-1):
    isquare = i**2
    for j in range(isquare, max_num+1, isquare):
        if not squares[j] % isquare:
            squares[j] //= isquare

for tc in range(1, T+1):
    print(f'#{tc} {squares[ls[tc-1]]}')
N = int(input())
if N % 2 == 0: ls = [x for x in range (1, int(N/2) + 1) if N % x == 0]
else: ls = [x for x in range (1, int(N/3)+1) if N % x == 0]

print(*ls, N)
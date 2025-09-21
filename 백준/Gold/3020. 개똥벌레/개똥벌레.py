import sys
input = sys.stdin.readline

n, h = map(int, input().split())
imos = [0] * (h+1)  # h까지 둬야 범위 끝에서 -1 처리 가능

for _ in range(n//2):
    # 석순 (아래에서 올라옴)
    x = int(input())
    imos[0] += 1
    imos[x] -= 1

    # 종유석 (위에서 내려옴)
    y = int(input())
    imos[h-y] += 1
    imos[h] -= 1

# 누적합으로 각 높이마다 걸리는 장애물 개수 계산
for i in range(1, h):
    imos[i] += imos[i-1]

ans, count = 500000, 0

for k in range(h):
    curr = imos[k]
    if ans > curr:
        ans = curr
        count = 1
    elif ans == curr:
        count += 1

print(ans, count)
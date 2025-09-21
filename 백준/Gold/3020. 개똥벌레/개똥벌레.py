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
curr = 0
result = []
for i in range(h):
    curr += imos[i]
    result.append(curr)

# 최소값과 개수 찾기
ans = min(result)
count = result.count(ans)
print(ans, count)

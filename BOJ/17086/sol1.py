N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
sharks = []
for i in range(N):
    for j in range(M):
        if board[i][j]: sharks.append((i,j))

max_safe = 0
for i in range(N):
    for j in range(M):
        if i==j: continue
        else: temp2 = max(abs(sharks[i][0]-sharks[j][0]),abs(sharks[i][1]-sharks[j][1]))  # 상어 간 이동해야 할 횟수
        if temp > temp2: temp = temp2       # 중에서 제일 작은 값이 그 자리가 가진 안전거리
    if max_safe < temp: max_safe = temp     # 상어가 가진 안전거리 중에서 제일 큰 거리가 max_safe
print(max_safe)

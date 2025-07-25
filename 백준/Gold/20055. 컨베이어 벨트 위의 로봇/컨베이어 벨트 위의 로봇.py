from collections import deque

n, k = map(int,input().split())
As = deque([0, a] for a in map(int,input().split()))
ans = 0
cnt = 0

# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
while cnt < k:
    ans += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    As.rotate(1)
    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    As[n-1][0]=0
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, 0, -1):
        # - 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        if As[i][0] and not As[i+1][0] and As[i+1][1]:
            As[i][0] = 0
            As[i+1][0] = 1
            As[i+1][1] -= 1
            if not As[i+1][1]:
                cnt += 1
    As[n-1][0]=0
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if As[0][1]:
        As[0][0] = 1
        As[0][1] -= 1
        if not As[0][1]:
            cnt +=1

print(ans)
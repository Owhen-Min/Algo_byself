def DFS(curr_p, curr_e, visited, level):       # 현재 위치, 현재 들어간 에너지, 방문한 장소
    global min_bat
    if curr_e > min_bat:
        return
    elif level == N:
        curr_e += club[curr_p][0]
        if min_bat > curr_e:
            min_bat = curr_e
            return
    else:
        for i in range(1, N):
            if visited[i]: continue
            else:
                visited[i] = 1
                DFS(i, curr_e + club[curr_p][i], visited, level +1)
                visited[i] = 0


T= int(input())

for tc in range(1, T+1):
    N = int(input())
    club = [list(map(int, input().split())) for _ in range(N)]
    min_bat = 999999
    v = [0] * (N)
    DFS(0,0,v,1)
    print(f'#{tc} {min_bat}')

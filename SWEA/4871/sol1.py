def DFS(s,g):
    stack = []
    ans = 0
    visited = [0]*len(matrix)
    for x in range(1,len(matrix)):
        if matrix[s][x]: stack.append(x)
    while stack:
        temp = stack.pop()
        if temp == g:
            ans = 1
            break
        for x in range(1,len(matrix)):
            if not visited[temp] and matrix[temp][x]: stack.append(x)
        visited[temp]= 1
    return ans

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int,input().split())
        matrix[i][j] = 1

    s, g = map(int,input().split())
    print(f'#{tc} {DFS(s,g)}')


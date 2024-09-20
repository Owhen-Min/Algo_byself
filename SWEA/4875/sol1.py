T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    delta = [[0,1], [-1,0], [0,-1],[1,0]]

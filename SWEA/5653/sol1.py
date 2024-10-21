from collections import deque

T = int(input())
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
for tc in range (1, T+1):
    n, m, k = map(int,input().split())
    dir = dict()
    que = deque()
    for i in range(n):
        ls = list(map(int, input().split()))
        for j in range(m):
            if ls[j]:
                # y 좌표, x좌표, 활성화 시간(at), 죽는 시간(dt), 생명력)
                dir[(i, j)] = (ls[j], ls[j] * 2, ls[j])
                que.append((i,j))
                # {(0, 0): (1, 2, 1), (0, 1): (1, 2, 1), (1, 1): (2, 4, 2)}
    while que:
        
    # t = 1
    # while t <= k:
    #     for elem in st:
    #

'''
3
2 2 10
1 1
0 2
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
9 10 37                
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 5 3
0 0 2 0 0 0 0 4 0 0
3 0 0 0 0 0 4 0 0 0
0 0 0 0 0 3 5 0 0 2
0 0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 2 3
0 0 0 0 0 0 0 0 0 0
0 0 2 2 0 0 0 0 0 0
'''
from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int,input().split())
    q = deque(map(int,input().split()))
    for i in range(m):
        c, *data = input().split()

        if c == 'I':
            q.insert(int(data[0]), int(data[1]))
        elif c == 'C':
            q[int(data[0])] = int(data[1])
        elif c == 'D':
            del q[int(data[0])]
    if l > len(q):
        ans = -1
    else:
        ans = q[l]
    print(f'#{tc} {ans})
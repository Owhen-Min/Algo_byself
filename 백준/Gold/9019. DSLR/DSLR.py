from collections import deque

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10000
    path = [""] * 10000
    
    q = deque([a])
    visited[a] = True
    
    while q:
        curr = q.popleft()
        
        if curr == b:
            break
        
        # D
        d = (2 * curr) % 10000
        if not visited[d]:
            visited[d] = True
            path[d] = path[curr] + "D"
            q.append(d)
        
        # S
        s = (curr - 1) % 10000
        if not visited[s]:
            visited[s] = True
            path[s] = path[curr] + "S"
            q.append(s)
        
        # L
        l = (curr % 1000) * 10 + curr // 1000
        if not visited[l]:
            visited[l] = True
            path[l] = path[curr] + "L"
            q.append(l)
        
        # R
        r = (curr % 10) * 1000 + curr // 10
        if not visited[r]:
            visited[r] = True
            path[r] = path[curr] + "R"
            q.append(r)
    
    print(path[b])
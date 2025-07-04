for _ in range(int(input())):
    n = int(input())
    nxt = [x-1 for x in map(int, input().split())]
    
    # -1=미방문, 0 이상=방문 시점
    visited = [-1] * n
    on_stack = [False] * n
    cycle_nodes = 0
    
    for start in range(n):
        if visited[start] != -1:
            continue
            
        curr = start
        time = 0
        
        # DFS 탐색
        while visited[curr] == -1:
            visited[curr] = time
            on_stack[curr] = True
            time += 1
            curr = nxt[curr]
            
        # 사이클 발견
        if on_stack[curr]:
            cycle_nodes += time - visited[curr]
            
        # 스택에서 노드 제거
        curr = start
        while on_stack[curr]:
            on_stack[curr] = False
            curr = nxt[curr]
    
    print(n - cycle_nodes)
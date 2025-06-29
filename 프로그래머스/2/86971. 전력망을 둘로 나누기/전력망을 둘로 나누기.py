from collections import defaultdict

def dfs(node, dd, visited):
    visited[node] = 1
    cnt = 1
    
    for nxt in dd[node]:
        if not visited[nxt]:
            cnt += dfs(nxt, dd, visited)
    
    return cnt

def solution(n, wires):
    answer = n
    dd = defaultdict(list)
    for p, c in wires:
        dd[p].append(c)
        dd[c].append(p)
    
    for p, c in wires:
        dd[p].remove(c)
        dd[c].remove(p)
        answer = min(answer,abs(n-2*dfs(p, dd, [0]*(n+1))))
        dd[p].append(c)
        dd[c].append(p)
    return answer
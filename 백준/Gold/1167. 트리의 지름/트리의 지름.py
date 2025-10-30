import sys
input = sys.stdin.readline

def find_farthest(start_node):
    visited = [False] * (v+1)
    visited[start_node] = True
    stack = [(start_node,0)]
    max_dist = 0
    farthest_node = 0
    while stack:
        curr, dist = stack.pop()
        for nxt, cost in adj[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, dist + cost))
        if dist > max_dist:
            max_dist = dist
            farthest_node = curr
    return farthest_node, max_dist

v = int(input())
adj = {i:[] for i in range(1, v+1)}

# 인접 그래프 그리기
for _ in range(v):
    a, *links = map(int,input().split())
    i = 0
    while True:
        if links[i] == -1:
            break
        adj[a].append((links[i], links[i+1]))
        i += 2

# 임의의 노드에서 제일 먼 거리의 노드 찾기
nxt, dist = find_farthest(1)

# 그 노드에서 제일 먼 거리의 노드 찾기
target, ans = find_farthest(nxt)


print(ans)
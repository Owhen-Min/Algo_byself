from collections import defaultdict


def dfs(c_node, t_node, cost, visited):
    if c_node == t_node:
        return cost
    elif routes[c_node]:
        for n_node in routes[c_node]:
            if n_node not in visited:
                visited.add(n_node)
                return dfs(n_node, t_node, cost+int(routes[c_node][n_node]), visited)
    else: return 'NO'


T = int(input())
for tc in range(1, T+1):
    routes = defaultdict(dict)
    for _ in range(int(input().strip())):
        route = input().strip().split()
        routes[route[0]][route[1]] = route[2]       # defaultdict(<class 'dict'>, {'a': {'z': '100'}, 'z': {'A': '100'}, 'A': {'Z': '100'}})
    ans = dfs('a', 'Z', 0, set())

    if type(ans)==int:
        print(f'#{tc} YES {ans}')
    else:
        print(f'#{tc} {ans}')
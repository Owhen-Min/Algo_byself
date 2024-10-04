from collections import deque


def solution(info, edges):
    answer = 0
    routes = [[] for _ in range(len(info))]
    for s, e in edges:
        routes[s].append(e)
    q = deque()
    sheep = 1
    wolves = 0
    q += routes[0]
    q += routes[1]
    print(q)

    return answer



solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
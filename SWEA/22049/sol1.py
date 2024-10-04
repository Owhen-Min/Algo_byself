from collections import defaultdict, deque

def riding(st):
    global max_result, visited
    if not visited[st]:
        value = ls[st-1]
        visited[st]= 1
    else:
        return
    subnodes = deque()
    subnodes.extend(start[st])
    while subnodes:
        new = subnodes.popleft()
        subnodes.extend(start[new])
        riding(new)
        value += ls[new-1]

    if max_result < value:
        max_result = value


T = int(input())
for tc in range(T):
    N = int(input())
    ls = list(map(int,input().split()))
    max_result = 0
    start1 = defaultdict(set)
    end1 = defaultdict(set)
    start2 = defaultdict(set)
    end2 = defaultdict(set)
    visited1 = [0]*(N+1)
    visited2 = [0]*(N+1)
    for i in range(N-1):
        s, e = map(int,input().split())
        start1[s].add(e)
        end1[e].add(s)
    for i in range(N-1):
        s, e = map(int,input().split())
        start2[s].add(e)
        end2[e].add(s)

    for i in range(1, N+1):
        if i not in end1.keys():
            riding(i)
    print(max_result)
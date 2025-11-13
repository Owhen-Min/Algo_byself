from collections import deque

n, k = map(int,input().split())

if n >= k:
    print(n-k)
    exit()

max_length = max(n,k)
visited = [max_length]*int(max_length*1.2+1)
visited[n] = 0
q = deque([n])

while q:
    curr = q.popleft()
    curr_time = visited[curr]
    try:
        if visited[curr*2] > visited[curr]:
            visited[curr*2] = curr_time
            q.append(curr*2)
    except IndexError:
        pass
    try:
        if visited[curr+1] > visited[curr]+1:
            visited[curr+1] = curr_time+1
            q.append(curr+1)
    except IndexError:
        pass
    try:
        if visited[curr-1] > visited[curr]+1:
            visited[curr-1] = curr_time+1
            q.append(curr-1)
    except IndexError:
        pass


print(visited[k])
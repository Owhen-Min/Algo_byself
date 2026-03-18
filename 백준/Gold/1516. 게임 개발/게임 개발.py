import heapq

n = int(input())
proc = [0]*n
trail = {i:[] for i in range(n)}
build_time = [0]*n
built_time = [0]*n

for i in range(n):
    bt, *ls = map(int,input().split())
    build_time[i] = bt

    for c in ls:
        if c != -1:
            trail[c-1].append(i)
            proc[i] +=1

inbuild = list((build_time[i], i) for i in range(n) if not proc[i])
heapq.heapify(inbuild)

while inbuild:
    curr, building = heapq.heappop(inbuild)
    built_time[building] = curr

    for nxt in trail[building]:
        proc[nxt] -= 1
        if proc[nxt] == 0:
            heapq.heappush(inbuild, (curr+build_time[nxt], nxt))

print(*built_time, sep = "\n")
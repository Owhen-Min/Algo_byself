n, k, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

e = [0]*(n)
for i in map(int, input().split()):
    e[i-1]+=1
    if i+l <= n:
        e[i+l-1] -= 1

for i in range(1,n):
    e[i] += e[i-1]
e.sort()

result = sum(h[j] >> e[j] for j in range(n) if e[j] <30)
print(result)
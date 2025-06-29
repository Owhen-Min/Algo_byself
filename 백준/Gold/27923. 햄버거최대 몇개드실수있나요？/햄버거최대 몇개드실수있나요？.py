n, k, l = map(int, input().split())

diff = [0]*n

m = sorted(map(int, input().split()))

for num in map(int,input().split()):
    try:
        diff[num-1] += 1
        diff[num+l-1] -= 1
    except IndexError:
        pass

for i in range(n-1):
    diff[i+1] += diff[i]

diff.sort()

ans = 0

for i in range(n):
    ans += m[i]//(2**diff[i])

print(ans)
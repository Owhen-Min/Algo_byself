import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
diff = [0] * n
m = sorted(map(int, input().split()))

for num in map(int, input().split()):
    diff[num-1] += 1
    if num + l <= n:
        diff[num+l-1] -= 1

for i in range(1, n):
    diff[i] += diff[i-1]

diff.sort()

result = 0
for i in range(n):
    result += m[i] >> diff[i]
print(result)

import sys
input = sys.stdin.readline

n = int(input())
piles = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
    exit()

piles.sort()
from collections import deque
orig = deque(piles)
new = deque()

ans = 0

def pop_min():
    if orig and new:
        return orig.popleft() if orig[0] < new[0] else new.popleft()
    elif orig:
        return orig.popleft()
    else:
        return new.popleft()

while len(orig) + len(new) > 1:
    a = pop_min()
    b = pop_min()
    total = a + b
    ans += total
    new.append(total)

print(ans)

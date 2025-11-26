import sys
input = sys.stdin.readline
from array import array

n = int(input())
A, B, C, D = array("i"), array("i"), array("i"), array("i")

for _ in range(n):
    a, b, c, d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = array("i", sorted(a+b for a in A for b in B))
CD = array("i", sorted(c+d for c in C for d in D))

l = len(CD)
left = 0
right = l-1

ans = 0

while left < l and right >= 0:
    curr = AB[left] + CD[right]
    if curr < 0:
        left += 1
    elif curr > 0:
        right -= 1
    else:
        bunch_left = bunch_right = 1
        while left < l-1 and AB[left] == AB[left+1]:
            left +=1
            bunch_left +=1
        while right > 0 and CD[right] == CD[right-1]:
            right -= 1
            bunch_right +=1
        left+=1
        right -=1
        ans += bunch_left * bunch_right

print(ans)
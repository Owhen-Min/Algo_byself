import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
friends_fee = list(map(int,input().split()))

parents = list(range(n))

def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    p1, p2 = find(node1), find(node2)
    if p2 < p1: parents[p1] = p2
    else: parents[p2] = p1


for _ in range(m):
    n1, n2 = map(int,input().split())
    union(n1-1, n2-1)

price_dict = dict()

for i in range(n):
    curr = find(i)
    if price_dict.setdefault(curr, 10000) > friends_fee[i]:
        price_dict[curr] = friends_fee[i]
ans = sum(price_dict.values())

print(ans if ans <= k else "Oh no")
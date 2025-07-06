from collections import defaultdict

n, k = map(int,input().split())

dd = defaultdict(int)
dd[0] = 0

objects = tuple(map(int,input().split()) for _ in range(n))

for w, v in objects:
    new_d = dict()
    prev_items = dict(dd.items())
    for old_w, old_v in prev_items.items():
        if w+old_w <= k and v+old_v > dd[w+old_w]:
            new_d[w+old_w]= v+old_v
    dd.update(new_d)

print(max(dd.values()))
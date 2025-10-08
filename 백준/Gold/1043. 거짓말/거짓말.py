n, m = map(int,input().split())
a, *knowers = map(int,input().split())
knowers = set(knowers)

parties = [list(map(int,input().split()))[1:] for _ in range(m)]

prev = 0
while len(knowers) != prev:
    prev = len(knowers)
    for party in parties:
        if any(part in knowers for part in party):
            knowers.update(party)

ans = 0

for party in parties:
    if all(part not in knowers for part in party):
        ans += 1

print(ans)
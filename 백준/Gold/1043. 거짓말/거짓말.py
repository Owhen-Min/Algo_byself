from collections import defaultdict

n, m = map(int, input().split())
known, *watchers = map(int, input().split())
watchers = set(watchers)
visited = [0] * (n+1)
party_dict = dict()
person_party_dict = defaultdict(list)
only_truth_party = set()

for i in range(m):
    num, *participants = map(int, input().split())
    party_dict[i] = participants
    for participant in participants:
        person_party_dict[participant].append(i)

while True:
    for watcher in watchers:
        if visited[watcher]:
            continue
        else:
            visited[watcher] = 1
            only_truth_party.update(person_party_dict[watcher])
            for party in person_party_dict[watcher]:
                watchers.update(party_dict[party])
            break
    else:
        break

print(m-len(only_truth_party))
def is_shared_properly(p, cards):
    if all(p[cards[i]] == (i % 3) for i in range(n)):
        return True
    else:
        return False

def shuffle(cards):
    shuffled = [0] * n
    for j in range(n):
        shuffled[s[j]] = cards[j]
    return shuffled


n = int(input())
p = list(map(int,input().split()))
s = list(map(int,input().split()))
cards = [i for i in range(n)]

if is_shared_properly(p, cards):
    print(0)
else:
    initial = cards
    cards = shuffle(cards)
    # k = 카드를 섞은 횟수
    k = 0
    while initial != cards:
        k += 1
        if is_shared_properly(p, cards):
            print(k)
            break
        cards = shuffle(cards)
    else:
        print(-1)

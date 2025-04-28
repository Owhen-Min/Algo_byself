from itertools import permutations

n = int(input())
posses = tuple(poss[:3] + (0,) + poss[3:] for poss in permutations(range(1, 9), 8))
innings = tuple(tuple(map(int, input().split())) for _ in range(n))
best_score = 0

for poss in posses:
    score = 0
    curr_inning = 0
    curr_batter_index = 0

    while curr_inning < n:
        outs = 0
        b1 = b2 = b3 = 0
        while outs < 3:
            curr_batter = poss[curr_batter_index]
            output = innings[curr_inning][curr_batter]
            curr_batter_index = (curr_batter_index + 1) % 9
            if output == 0:
                outs += 1
            elif output == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif output == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif output == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            else:
                score += b3 + b2 + b1 + 1
                b1 = b2 = b3 = 0
        curr_inning += 1

    best_score = max(best_score, score)

print(best_score)
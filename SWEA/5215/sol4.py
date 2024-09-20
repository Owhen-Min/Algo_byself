# 메모리 초과


from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    scores = []
    cals = []
    for i in range(N):
        score, cal = map(int, input().split())
        scores.append(score)
        cals.append(cal)

    max_score = 0
    subset_score = []
    subset_cal = []
    for i in range(1, N + 1):
        subset_score += list(combinations(scores, i))
        subset_cal += list(combinations(cals, i))

    subset_score = list(map(sum,subset_score))
    subset_cal = list(map(sum,subset_cal))

    for i in range((1<<N) -1):
        if subset_cal[i] <= L and max_score < subset_score[i]:
            max_score = subset_score[i]

    print(f'#{tc} {max_score}')
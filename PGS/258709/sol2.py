from itertools import combinations, product


def solution(dice):
    dices = list(range(len(dice)))
    A_dices = list(combinations(dices, len(dice) // 2))
    best_comb = None
    best_win_cases = 0
    for A_dice in A_dices:
        B_dice = [x for x in dices if x not in A_dice]
        A = [dice[i] for i in A_dice]
        B = [dice[i] for i in B_dice]
        A_results = sorted(map(sum, product(*A)))
        B_results = sorted(map(sum, product(*B)))
        win_cases = 0
        i = 0

        while i < len(A_results):
            j = 0
            while j < len(B_results) and A_results[i] > B_results[j]:
                j += 1
            win_cases += j
            i += 1

        if best_win_cases < win_cases:
            best_comb = list(map(lambda x: x + 1, A_dice))
            best_win_cases = win_cases

    return list(best_comb)
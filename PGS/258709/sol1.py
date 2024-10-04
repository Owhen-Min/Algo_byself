from itertools import combinations, product


def solution(dice):
    dices = list(range(len(dice)))
    A_dices = list(combinations(dices, len(dice) // 2))
    B_dices = [[x for x in dices if x not in A_dice] for A_dice in A_dices]
    best_comb = None
    best_win_cases = 0
    for A_dice, B_dice in zip(A_dices, B_dices):
        A = [dice[i] for i in A_dice]
        B = [dice[i] for i in B_dice]
        A_results = list(map(sum, product(*A)))
        B_results = list(map(sum, product(*B)))
        win_cases = 0
        for a in A_results:
            for b in B_results:
                if a > b:
                    win_cases += 1
        if best_win_cases < win_cases:
            best_comb = list(map(lambda x: x + 1, A_dice))
            best_win_cases = win_cases

    return list(best_comb)



def simulate_game(order, innings):
    score = 0
    current_batter = 0  # 현재 타자를 가리키는 인덱스
    for inning in innings:
        outs = 0
        bases = [0, 0, 0, 0]  # 주자 베이스 상태
        while outs < 3:
            result = inning[order[current_batter]]
            if result == 0:  # 아웃
                outs += 1
            else:
                for _ in range(result):
                    bases[3] += bases[2]
                    bases[1:3] = bases[0:2]
                    bases[0] = 0
                bases[result - 1] += 1
            current_batter = (current_batter + 1) % 9  # 다음 타자로 이동
        score += bases[3]
    return score


def find_best_lineup(N, innings):
    max_score = 0
    used = [False] * 9
    lineup = [-1] * 9
    lineup[3] = 0  # 1번 타자는 4번 타자로 고정
    used[0] = True

    def generate_lineup(index):
        nonlocal max_score
        if index == 9:
            # 타순이 완성되면 점수 계산
            score = simulate_game(lineup, innings)
            max_score = max(max_score, score)
            return

        if index == 3:
            # 4번 타자는 이미 고정되어 있으므로 건너뜀
            generate_lineup(index + 1)
        else:
            for i in range(9):
                if not used[i] and i != 0:
                    used[i] = True
                    lineup[index] = i
                    generate_lineup(index + 1)
                    used[i] = False

    generate_lineup(0)
    return max_score


# 입력 받기
N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(find_best_lineup(N, innings))

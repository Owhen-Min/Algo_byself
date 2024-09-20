def work(task, burdened, cur_poss, max_poss):
    # case 1. 현재까지의 확률이 최대 확률보다 낮을 경우 나간다.
    if cur_poss <= max_poss:
        return max_poss
    # case 2. 작업을 모두 맡긴 경우에 max_poss를 갱신한다.
    elif task == N:
        return cur_poss
    # case 3. 작업을 다 맡기지 않았다면, 지금까지 일을 맡지 않은 직원에게 일을 맡긴다.
    else:
        for i in range(1, N+1):
            if not burdened[i]:
                burdened[i] = task+1
                max_poss = work(task+1, burdened, cur_poss*poss[task][i-1]*.01, max_poss)
                burdened[i] = 0
        return max_poss


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    poss = [list(map(int,input().split())) for _ in range(N)]
    max_prob = work(0,[0]*(N+1), 1, 0)
    print(f'#{tc} %.6f'%(max_prob*100))
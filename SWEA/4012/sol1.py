def div_ing(A_ing=set(),last=0):
    if len(A_ing)==(N//2):
        B_ing= set()
        for j in range(0,N):
            if j not in A_ing:
                B_ing.add(j)
        cook(A_ing,B_ing)
        return

    for i in range(last,N):
        A_ing.add(i)
        div_ing(A_ing,i+1)
        A_ing.discard(i)



def cook(A, B):
    score_A = score_B = 0

    for a in A:
        for a_ in A:
            if a!=a_:
                score_A += harmony[a][a_]

    for b in B:
        for b_ in B:
            if b!=b_:
                score_B += harmony[b][b_]

    global min_diff
    if min_diff > abs(score_A-score_B):
        min_diff = abs(score_A-score_B)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    harmony = [list(map(int,input().split())) for _ in range(N)]
    min_diff = 100000
    div_ing()
    print(f'#{tc} {min_diff}')
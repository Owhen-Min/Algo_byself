T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    ls = [0 for _ in range(N + 1)]    # 제출한 사람의 수를 체크하기 위한 ls. 0번 인덱스는 버린다.
    assignment = list(map(int,input().split()))
    for i in range(K):
        ls[assignment[i]] += 1
    print(f'#{tc}', end= ' ')
    for i in range(1, N+1):
        if ls[i]==0: print(i, end= ' ')
    print()

MOD = 10 ** 9 + 7


def build_sparse_table(arr):
    N = len(arr)
    log = [0] * (N + 1)
    for i in range(2, N + 1):
        log[i] = log[i // 2] + 1

    K = log[N] + 1
    st = [[0] * K for _ in range(N)]

    for i in range(N):
        st[i][0] = arr[i]

    j = 1
    while (1 << j) <= N:
        i = 0
        while (i + (1 << j) - 1) < N:
            st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1

    return st, log


def query_max(st, log, L, R):
    j = log[R - L + 1]
    return max(st[L][j], st[R - (1 << j) + 1][j])


def count_valid_quadruples(arr):
    N = len(arr)
    if N < 4:
        return 0

    st, log = build_sparse_table(arr)

    cnt = 0

    for i in range(N):
        for j in range(i, N):
            max1 = query_max(st, log, i, j)
            for k in range(j + 1, N):
                for l in range(k, N):
                    max2 = query_max(st, log, k, l)
                    if max1 == max2:
                        cnt += 1
                if cnt >= MOD:
                    cnt %= MOD

    return cnt

T = int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = list(map(int,input().split()))
    print(count_valid_quadruples(arr))
from functools import lru_cache


def check(mat, W, K):
    for i in range(W):
        row = ''.join(mat[i])
        if len(max(row.split('0'))) < K and len(max(row.split('1'))) < K:
            return False
    return True


@lru_cache(None)
def inject_chem(mat, index, tries, chem, min_try, D, K):
    if tries >= min_try:
        return min_try

    new_mat = [x[:index] + [str(chem)] + x[index + 1:] for x in mat]

    if check(new_mat, len(mat), K):
        return tries

    for i in range(index + 1, D):
        min_try = min(min_try,
                      inject_chem(tuple(map(tuple, new_mat)), i, tries + 1, 0, min_try, D, K),
                      inject_chem(tuple(map(tuple, new_mat)), i, tries + 1, 1, min_try, D, K))
    return min_try


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    films = [input().split() for _ in range(D)]
    films_T = list(map(list, zip(*films)))

    min_t = inject_chem(tuple(map(tuple, films_T)), 0, 0, 0, float('inf'), D, K)
    print(f'#{tc} {min_t}')
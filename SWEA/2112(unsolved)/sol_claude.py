from functools import lru_cache


def inject_chem(mat, index, tries, chem, min_try):
    if tries >= min_try:
        return min_try

    new_mat = tuple(row[:index] + (str(chem),) + row[index + 1:] for row in mat)

    if check(new_mat):
        return tries

    for i in range(index + 1, D):
        min_try = min(min_try, inject_chem(new_mat, i, tries + 1, 0, min_try))
        min_try = min(min_try, inject_chem(new_mat, i, tries + 1, 1, min_try))

    return min_try


@lru_cache(maxsize=None)
def check(mat):
    return all(
        any(all(mat[i + k][j] == mat[i][j] for k in range(K)) for i in range(D - K + 1))
        for j in range(W)
    )


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    films = tuple(tuple(input().split()) for _ in range(D))
    films_T = tuple(zip(*films))

    if check(films_T):
        min_t = 0
    else:
        min_t = min(inject_chem(films_T, 0, 1, 0, K),
                    inject_chem(films_T, 0, 1, 1, K))

    print(f'#{tc} {min_t}')
def inject_chem(mat, index, tries, chem, found, max_try = 0):
    if found:
        return found

    elif tries:
        new_mat = [x[:index]+[str(chem)]+x[index+1:] for x in mat]

        if tries == max_try:
            return check(new_mat)

        else:
            for i in range(index+1,D):
                found = inject_chem(new_mat, i, tries + 1, 0, found, max_try)
                found = inject_chem(new_mat, i, tries + 1, 1, found, max_try)

            return found

    else:
        if check(mat):
            return tries
        i = 1
        while not found:
            for j in range(D):
                found = inject_chem(mat, j, tries + 1, 0, found, i)
                found = inject_chem(mat, j, tries + 1, 1, found, i)
            i += 1
        return i-1


def check(mat):
    for i in range(W):
        if not (len(max(''.join(mat[i]).split('0'))) >= K or len(max(''.join(mat[i]).split('1'))) >= K):
            return False
    else: return True


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int,input().split())
    films = [list(input().split()) for _ in range(D)]
    films_T = list(map(list,zip(*films)))
    min_t = inject_chem(films_T, 0, 0, 0, False)
    print(f'#{tc} {min_t}')

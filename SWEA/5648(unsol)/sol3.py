def check(A, B):
    xa, ya, da, e = atoms[A]
    xb, yb, db, e = atoms[B]

    dx = xb- xa
    dy = yb- ya

    if dx == 0:
        if da == 0 and db ==1:
            result.append([dy, A, B])
    elif dy == 0:
        if da == 3 and db == 2:
            result.append([dx, A, B])
    elif dx == dy:
        if (da == 3 and db == 1) or (da==0 and db==2):
            result.append([2*dx, A, B])
    elif dx == -dy:
        if (da == 1 and db == 2) or (da==3 and db ==0):
            result.append([2*dx, A, B])


def collide():
    collisions = [0] * N
    energy = 0

    for diff, A, B in result:
        if collisions[A] == 0 and collisions[B] in [0, diff]:
            energy += atoms[A][3]
            collisions[A] = diff
        if collisions[B] == 0 and collisions[A] in [0, diff]:
            energy += atoms[B][3]
            collisions[B] = diff
    return energy


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]
    atoms.sort()
    result = []
    for i in range(N-1):
        for j in range(i+1,N):
            check(i, j)

    result.sort()

    energy = collide()
    print(f'#{tc} {energy}')
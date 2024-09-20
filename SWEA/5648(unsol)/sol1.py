T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]
    gone = [0] * N
    dists = [4000] * N
    energy = 0
    min_anchor = 0
    while min_anchor != 4001:
        for i in range(N-1):
            anchor = 0
            anchor_i = 0
            min_anchor = 4001
            if not gone[i]:
                for j in range(i+1,N):
                    if not gone[j]:
                        if atoms[i][2] == atoms[j][2]:
                            continue
                        elif atoms[i][2] == 0:
                            if atoms[i][1]<atoms[j][1]:
                                if atoms[j][2] == 1:
                                    if atoms[i][0] == atoms[j][0]:
                                        if anchor > abs(atoms[i][1]-atoms[j][1]):
                                            anchor = (abs(atoms[i][1]-atoms[j][1]))//2
                                            anchor_i = j
                                elif atoms[j][2] == 2:
                                    if atoms[j][0] - atoms[i][0] == atoms[j][1] - atoms[j][1]:
                                        if anchor > abs(atoms[i][1]-atoms[j][1]):
                                            anchor = abs(atoms[i][1]-atoms[j][1])
                                            anchor_i = j
                                elif atoms[j][2] == 3:
                                    if atoms[i][0] - atoms[j][0] == atoms[j][1] - atoms[i][1]:
                                        if anchor > abs(atoms[i][1]-atoms[j][1]):
                                            anchor = abs(atoms[i][1]-atoms[j][1])
                                            anchor_i = j

                        elif atoms[i][2] == 1:
                            if atoms[i][1]>atoms[j][1]:
                                if atoms[j][2] == 0:
                                    if atoms[i][0] == atoms[j][0]:
                                        if not anchor:
                                            anchor = (abs(atoms[i][1] - atoms[j][1]))//2
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][1]-atoms[j][1]):
                                            anchor = (abs(atoms[i][1]-atoms[j][1]))//2
                                            anchor_i = j
                                elif atoms[j][2] == 2:
                                    if atoms[j][0] - atoms[i][0] == atoms[i][1] - atoms[j][1]:
                                        if not anchor:
                                            anchor = abs(atoms[i][1] - atoms[j][1])
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][1]-atoms[j][1]):
                                            anchor = abs(atoms[i][1]-atoms[j][1])
                                            anchor_i = j
                                elif atoms[j][2] == 3:
                                    if atoms[i][0] - atoms[j][0] == atoms[i][1] - atoms[j][1]:
                                        if not anchor:
                                            anchor = abs(atoms[i][1] - atoms[j][1])
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][1]-atoms[j][1]):
                                            anchor = abs(atoms[i][1]-atoms[j][1])
                                            anchor_i = j

                        elif atoms[i][2] == 2:
                            if atoms[i][0]>atoms[j][0]:
                                if atoms[j][2] == 3:
                                    if atoms[i][1] == atoms[j][1]:
                                        if not anchor:
                                            anchor = (abs(atoms[i][1] - atoms[j][1]))//2
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][0]-atoms[j][0]):
                                            anchor = (abs(atoms[i][0]-atoms[j][0]))//2
                                            anchor_i = j
                                elif atoms[j][2] == 0:
                                    if atoms[i][0] - atoms[j][0] == atoms[i][1] - atoms[j][1]:
                                        if not anchor:
                                            anchor = abs(atoms[i][1] - atoms[j][1])
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][0]-atoms[j][0]):
                                            anchor = abs(atoms[i][0]-atoms[j][0])
                                            anchor_i = j
                                elif atoms[j][2] == 1:
                                    if atoms[i][0] - atoms[j][0] == atoms[j][1] - atoms[i][1]:
                                        if not anchor:
                                            anchor = abs(atoms[i][1] - atoms[j][1])
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][0]-atoms[j][0]):
                                            anchor = abs(atoms[i][0]-atoms[j][0])
                                            anchor_i = j

                        else:
                            if atoms[i][0] < atoms[j][0]:
                                if atoms[j][2] == 2:
                                    if atoms[i][1] == atoms[j][1]:
                                        if not anchor:
                                            anchor = (abs(atoms[i][0] - atoms[j][0]))//2
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][0]-atoms[j][0]):
                                            anchor = (abs(atoms[i][0]-atoms[j][0]))//2
                                            anchor_i = j
                                elif atoms[j][2] == 0:
                                    if atoms[j][0] - atoms[i][0] == atoms[i][1] - atoms[j][1]:
                                        if not anchor:
                                            anchor = abs(atoms[i][1] - atoms[j][1])
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][0]-atoms[j][0]):
                                            anchor = abs(atoms[i][0]-atoms[j][0])
                                            anchor_i = j
                                elif atoms[j][2] == 1:
                                    if atoms[j][0] - atoms[i][0] == atoms[j][1] - atoms[i][1]:
                                        if not anchor:
                                            anchor = abs(atoms[i][1] - atoms[j][1])
                                            anchor_i = j
                                        elif anchor > abs(atoms[i][0]-atoms[j][0]):
                                            anchor = abs(atoms[i][0]-atoms[j][0])
                                            anchor_i = j

                if not anchor: gone[i] = 1
                elif dists[i] >= anchor:
                    if min_anchor >= anchor:
                        dists[i] = dists[anchor_i] = anchor
                        min_anchor = anchor
        for i in range(N):
            if not gone[i] and dists[i] == min_anchor:
                gone[i] = 1
                energy += atoms[i][3]


    print(f'#{tc} {energy}')
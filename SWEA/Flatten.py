def mintoleft(ls):
    for i in range (len(ls)-1,0,-1):
        if ls[i]<ls[i-1]:
            ls[i], ls[i-1] = ls[i-1], ls[i]

def maxtoright(ls):
    0

for tc in range (1, 11):
    dumps = int(input())
    land = list(map(int,input().split()))
    for dump in range(dumps):
        mintoleft(land)
        maxtoright(land)
        if land[-1]-land[0] <= 1:
            print(f'#{tc} {land[-1]-land[0]}')
            continue
        land[-1] -= 1
        land[0] += 1
    mintoleft(land)
    maxtoright(land)
    print(f'#{tc} {land[-1] - land[0]}')
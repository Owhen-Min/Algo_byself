T= int(input())
Ns = [int(input()) for _ in range(T)]
pibbo = [0]*max(Ns)
pibbo[0] = pibbo[1] = 1
for i in range(max(Ns)-2):
    pibbo[i+2] = pibbo[i+1] + pibbo[i]

for N in Ns:
    i = 0
    total = sum(pibbo[:N])
    half = total /2
    while half > 0:
        half -= pibbo[i]
        i+=1
        if not half:
            print('B'*i+'A'*(N-i))
            break
    else: print('impossible')
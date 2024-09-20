T = int(input())
for tc in range (1, T+1):
    N, M, K = map(int,input().split())
    customers = list(map(int,input().split()))
    time = M-1
    m_time = 0
    balance = 0
    possible = True
    while customers:
        for i in range(len(customers)-1,-1,-1):
            if customers[i] <= time:
                balance -= 1
                customers.pop(i)
        if balance < 0:
            possible = False
            break
        time += M
        balance += K
    ls = ['Impossible','Possible']
    print(f'#{tc} {ls[possible]}')


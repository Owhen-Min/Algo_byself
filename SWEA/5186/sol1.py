T = int(input())
for tc in range(1, T+1):
    num = float(input())
    dec = ''
    i = 0
    while i <=12 and num != 0:
        i += 1

        if num >= 2**(-i):
            num -= 2**(-i)
            dec += '1'
            if num == 0: break
        else:
            dec += '0'
    else: dec = 'overflow'
    print(f'#{tc} {dec}')
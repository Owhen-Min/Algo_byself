T = int(input())
for tc in range (1, T+1):
    cards = input()
    card_ls = [0]*10
    for card in cards:
        card_ls[int(card)] += 1
    
    for _ in range(2):
        for i in range(10):
            if card_ls[i] >= 3:
                card_ls[i] -=3
            if i+2<10 and card_ls[i] and card_ls[i+1] and card_ls[i+2]:
                card_ls[i] -=1
                card_ls[i+1] -=1
                card_ls[i+2] -=1
    
    if sum(card_ls) == 0:
        print(f'#{tc} 1')

    else: print(f'#{tc} 0')
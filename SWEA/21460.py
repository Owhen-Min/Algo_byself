    T = int(input())
    for tc in range(1, T+1):
        length = int(input())
        cards = list(map(int,input()))
        frequency = [0]*10
        for card in cards:
            frequency[card] += 1
        reverse = frequency[::-1]
        print(f'#{tc} {9-reverse.index(max(reverse))} {max(reverse)}')
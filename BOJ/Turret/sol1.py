T = int(input())
for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if dist == 0 and r1 == r2:
        print(f'#{tc} -1')
    elif dist == 0 and r1 != r2:
        print(f'#{tc} 0')
    elif dist > (r1 + r2)**2:
        print(f'#{tc} 0')
    elif dist == (r1 + r2)**2:
        print(f'#{tc} 1')
    elif (r1 - r2)**2 < dist < (r1 + r2)**2:
        print(f'#{tc} 2')
    elif dist == (r1 - r2)**2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
T = int(input())
for tc in range(1, T+1):
    N= int(input())
    sheet = set()
    for i in range(N-1,-1,-1):
        new_num = int(input())
        if new_num in sheet:
            sheet.remove(new_num)
        else:
            sheet.add(new_num)
    print(f'#{tc} {len(sheet)}')
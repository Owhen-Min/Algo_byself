A, B = map(int, input().split())

if B == 3:
    if A ==1:
        print('A')
    else: print('B')
else:
    if B > A:
        print('B')
    else: print('A')
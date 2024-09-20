T = int(input())
for tc in range(1,T+1):
    N= int(input())
    dic = {}
    for _ in range(N):
        i = int(input())
        if i in dic.keys():
            dic.pop(i)
        else: dic.setdefault(i, 1)
    print(f'#{tc} {len(dic.keys())}')
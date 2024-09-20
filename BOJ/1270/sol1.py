T= int(input())
for tc in range(T):
    N, *ls = input().split()
    dic = {}
    for troop in ls:
        if troop in dic.keys():
            dic[troop] += 1
        else: dic[troop] = 1

    for key, value in dic.items():
        if value > int(N)//2:
            print(key)
            break
    else: print('SYJKGW')
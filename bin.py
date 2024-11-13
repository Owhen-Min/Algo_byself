n = int(input())
ls = sorted(map(int,input().split()))
target = int(input())
i = 0
j = n-1
cnt = 0

while i < j:
    if ls[i] + ls[j] < target:
        i += 1
    elif ls[i] + ls[j] > target:
        j-=1
    else:
        cnt +=1
        i += 1
print(cnt)
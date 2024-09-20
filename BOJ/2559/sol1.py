N, K = map(int,input().split())
ls = list(map(int,input().split()))
max_temp = temp = sum(ls[:K])
for i in range(0, N-K):
    temp = temp + ls[i+K] - ls[i]
    if max_temp < temp: max_temp = temp
print(max_temp)
n = int(input())
ls = list(map(int,input().split()))

i, j = 0, n-1

ans_pair = tuple()
ans_value = 1e10

while i < j:
    curr_value = ls[i] + ls[j]

    if ans_value > abs(curr_value):
        ans_value = abs(curr_value)
        ans_pair = (i, j)

    if curr_value > 0:j -=1
    else: i += 1

print(ls[ans_pair[0]], ls[ans_pair[1]])
T = int(input())
num_ls = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
    ls = [0]*5
    N = int(input())
    for i in range(5):
        while N % num_ls[i] == 0:
            N /= num_ls[i]
            ls[i] += 1
    print(f'#{tc}', *ls)

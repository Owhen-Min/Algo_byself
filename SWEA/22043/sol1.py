for tc in range(int(input())):
    N = int(input())
    numbers = [float(input()) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if numbers[i]*numbers[j] == int(numbers[i]*numbers[j]):
                cnt += 1
    print(cnt)
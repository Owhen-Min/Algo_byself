def solution(sequence):
    n = len(sequence)
    # 짝수번째 지수마다 -1을 곱한다. 반대의 경우는 음수를 곱하여 생각할 예정임.
    if n < 2:
        max_diff = abs(sequence[0])
    else:
        for i in range(1, n, 2):
            sequence[i] *= -1
        # 0번부터 쭉 더한 값을 list에 담는다. 그 앞에 있는 수를 빼면 부분합을 구할 수 있다.
        for i in range(1, n):
            sequence[i] += sequence[i - 1]

        min_num = sequence[-1]
        max_num = sequence[-1]
        max_diff = 0
        for i in range(n-1, -1, -1):
            if max_num < sequence[i]:
                max_num = sequence[i]
                max_diff = max(max_diff, -(min_num - max(0,max_num)))
            elif min_num > sequence[i]:
                min_num = sequence[i]
                max_diff = max(max_diff, max_num-min(0,min_num))
    return max_diff

print(solution([6, -7, 16, 3, -4]))
def solution(sequence):
    n = len(sequence)
    # 짝수번째 지수마다 -1을 곱한다. 반대의 경우는 음수를 곱하여 생각할 예정임.
    for i in range(1, n, 2):
        sequence[i] *= -1
    # 0번부터 쭉 더한 값을 list에 담는다. 그 앞에 있는 수를 빼면 부분합을 구할 수 있다.
    for i in range(1, n):
        sequence[i] += sequence[i - 1]

    max_num = max(sequence)
    if sequence.index(max_num):
        min_num = min(sequence[:sequence.index(max_num)])
    else:
        min_num = 0
    answer1 = max_num - min_num

    min_num2 = min(sequence)
    if sequence.index(min_num2):
        max_num2 = max(sequence[:sequence.index(min_num2)])
    else:
        max_num2 = 0
    answer2 = -(min_num2 - max_num2)

    if sequence.index(max_num) != n - 1:
        answer3 = -(min(sequence[sequence.index(max_num):]) - max_num)
    else:
        answer3 = 0

    if sequence.index(min_num2) != n - 1:
        answer4 = (max(sequence[sequence.index(min_num2):]) - min_num2)
    return max(answer1, answer2, answer3, answer4)
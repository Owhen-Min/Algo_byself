def solution(n, arr1, arr2):
    n_arr1 = []
    n_arr2 = []
    for num in arr1:
        s = ''
        for i in range(n):
            s += str(num % 2)
            num //= 2
        n_arr1.append(s)

    for num in arr2:
        s = ''
        for i in range(n):
            s += str(num % 2)
            num //= 2
        n_arr2.append(s)

    answer = []
    for i in range(n):
        s = ''
        for j in range(n):
            if n_arr1[i][j] == '#' or n_arr2[i][j] == '#':
                s += '#'
            else: s += ' '
        answer.append(s)
    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
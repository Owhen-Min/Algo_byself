def solution(n, info):
    answer = [0]*11
    weight = [0]*11
    for i in range(11):
        if info[i]:
            weight[i] = ((10-i) * 2 / (info[i]+1), 10-i)
        else:
            weight[i] = ((10-i), 10-i)
    weight.reverse()
    weight.sort(reverse=True)
    for dump, index in weight:
        if n > info[10-index]:
            answer[10-index] = info[10-index] +1
            n -= info[10-index]+1
    answer[10] = n
    a_score = 0
    r_score = 0
    for i in range(10):
        if answer[i] or info[i]:
            if answer[i] > info[i]:
                r_score += (10-i)
            else:
                a_score += (10-i)
    if a_score >= r_score:
        return [-1]
    else: return answer
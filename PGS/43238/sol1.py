def solution(n, times):
    enter = times.copy()
    n -= len(times)
    answer = 0

    while n != 0:
        answer += min(enter)
        enter = list(map(lambda x: x-min(enter), enter))
        for i in range(len(enter)):
            if not enter[i] and n:
                enter[i] = times[i]
                n -= 1
    enter = [times[i]+enter[i] if times[i] != enter[i] else times[i] for i in range(len(times))]
    answer += min(enter)
    return answer


solution(6, [7,10])
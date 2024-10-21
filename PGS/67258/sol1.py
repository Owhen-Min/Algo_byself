from collections import deque


def solution(gems):
    n= len(set(gems))
    q = deque()
    i= 0
    kinds = 0
    answer = deque()
    while True:
        pass
    answer = sorted(answer,key= lambda x: (x[1], x[0]))
    return answer[0]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
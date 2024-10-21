from collections import defaultdict

def solution(gems):
    n =len(set(gems))
    s_i = 0
    e_i = 0
    dic = defaultdict(int)
    ans = [[0,0],100000]
    while e_i != len(gems):
        dic[gems[e_i]]+=1
        if len(dic)== n:
            while dic[gems[s_i]] != 1:
                dic[gems[s_i]] -= 1
                s_i +=1
            del dic[gems[s_i]]
            if ans[1] > e_i - s_i:
                ans = [[s_i+1, e_i+1],e_i-s_i]
            s_i += 1
        e_i += 1
    return ans[0]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
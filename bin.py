from collections import defaultdict

def solution(fees, records):
    dic = defaultdict(list)
    for record in records:
        time, num, _ = record.split()
        dic[num].append(int(time[:2])*60+int(time[3:]))
    for key in dic:
        if len(dic[key])%2:
            dic[key].append(1439)
        temp = [0] * (len(dic[key])//2)
        for i in range(0, len(dic[key]),2):
            temp[i//2] = dic[key][i+1]-dic[key][i]
        dic[key] = temp
    # defaultdict(<class 'list'>, {'5961': [334, 479, 1379, 1380], '0000': [360, 394, 1139, 1439], '0148': [479, 1149]})
    print(dic)
    answer = []
    return answer


solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	)
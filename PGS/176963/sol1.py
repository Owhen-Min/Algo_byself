def solution(name, yearning, photo):
    answer = []
    for members in photo:
        sum = 0
        for member in members:
            if member in name:
                sum += yearning[name.find(member)]
        answer.append(sum)
    return answer
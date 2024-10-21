def solution(n, works):
    works.sort()
    # 배열의 길이 l
    l = len(works)
    # 배열의 마지막 두 번째 원소부터 아래로 깎아 나가자.
    for i in range(l-2,-1,-1):
        # i번째와 그 뒤의 차이가 존재한다면
        if works[i+1] - works[i]:




print(solution(4,[4, 3, 3]))
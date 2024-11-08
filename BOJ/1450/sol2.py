from itertools import combinations

# 모든 원소에 대해서 평가를 할 경우 최대 2^30의 시간복잡도가 나오므로 시간을 초과할 가능성이 높다.
# 따라서 Meet in the Middle이라는 알고리즘을 활용해서 2*2^15의 문제로 바꾸어, 투포인터 전략으로 문제를 접근할 경우 문제를 풀 수 있다.

n, c = map(int,input().split())
ls = list(map(int,input().split()))
# 좌우로 나누어 합을 구한 다음, DP를 활용하여 문제 해결할 예정.
left = ls[:n//2]
right = ls[n//2:]

# 리스트 컴프리헨션으로 각 부분집합의 합을 원소로 하는 두 개의 리스트를 만든다.
sum_left = sorted(elem for i in range(len(left)+1) for elem in list(map(sum,combinations(left, i))))
sum_right = sorted(elem for i in range(len(right)+1) for elem in list(map(sum,combinations(right, i))))

i = 0
j = len(sum_right)-1
# 최대 합을 구할 거니까 sum_left는 왼쪽에서, sum_right는 오른쪽에서 접근한다.
ans = 0
while i<len(sum_left):
    # 합이 c를 넘지 않는 최대값을 구하면, 그만큼의 케이스를 ans에 더해준다.
    if sum_left[i]+sum_right[j] <= c:
        ans += j+1
        i += 1
    # left의 값이 c를 넘어 right에서 어떤 값을 넣어도 통과할 수 없다면, 나간다.
    elif j < 0:
        break
    else:
        j -= 1
print(ans)

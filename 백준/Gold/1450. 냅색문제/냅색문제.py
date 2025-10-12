from itertools import combinations

n, c = map(int,input().split())
things = list(map(int,input().split()))

left, right = things[:n//2], things[n//2:]

# left_sums = 집합의 왼쪽 절반에서 나올 수 있는 모든 합들의 경우의 수
left_sums = sorted(elem for i in range(len(left)+1) for elem in map(sum, combinations(left, i)))
right_sums = sorted(elem for i in range(len(right)+1) for elem in map(sum, combinations(right, i)))

left_limit = len(left_sums)

i, j = 0, len(right_sums)-1

ans = 0

while i < left_limit and j >= 0:
    # 왼쪽 집단의 작은 애 + 오른쪽 집단의 큰 애를 비교
    curr = left_sums[i] + right_sums[j]
    if curr <= c:
        # 현재 왼쪽의 합 i에서는 오른쪽의 합 j보다 작은 애는 모두 가방에 넣을 수 있다
        ans += j+1
        i += 1
    else:
        # 오른쪽 집단에서 더 작은 애로 찾아본다.
        j -= 1

print(ans)
def dfs(numbers, count, k, visited):
    # 교환이 끝났을 때 최대값을 반환
    if count == k:
        return int("".join(numbers))

    max_val = 0
    n = len(numbers)

    # 이미 방문한 경우의 수는 중복 탐색하지 않음
    current_state = "".join(numbers) + str(count)
    if current_state in visited:
        return 0

    visited.add(current_state)

    # 모든 교환 가능한 쌍에 대해 시도
    for i in range(n):
        for j in range(i + 1, n):
            # i와 j를 교환
            numbers[i], numbers[j] = numbers[j], numbers[i]
            max_val = max(max_val, dfs(numbers, count + 1, k, visited))
            # 교환을 원래대로 되돌림
            numbers[i], numbers[j] = numbers[j], numbers[i]

    return max_val


def max_prize(tc, num_str, k):
    numbers = list(num_str)
    visited = set()
    max_value = dfs(numbers, 0, k, visited)
    print(f"#{tc} {max_value}")


# 테스트 케이스 입력
T = int(input())
for tc in range(1, T + 1):
    num_str, k = input().split()
    k = int(k)
    max_prize(tc, num_str, k)

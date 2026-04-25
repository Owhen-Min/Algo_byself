import sys

# 재귀 깊이 제한 해제 (n이 크므로)
sys.setrecursionlimit(2000)

n = int(input())
memo = {1: 0, 0: 0} # 기저 사례: 1이면 이동 횟수 0

def solve(v):
    if v in memo:
        return memo[v]
    
    # 1. v를 2의 배수로 만들어(v%2만큼 빼기) 2로 나누는 경우
    # 2. v를 3의 배수로 만들어(v%3만큼 빼기) 3으로 나누는 경우
    # 둘 중 최소값을 선택
    res = min(v % 2 + 1 + solve(v // 2), 
              v % 3 + 1 + solve(v // 3))
    
    memo[v] = res
    return res

print(solve(n))
'''
SSAFY 1학기에는 알고리즘 문제 풀이 이벤트를 진행한다.
이번에 좋은 기회가 되어 임스가 알고리즘 문제를 추천할 수 있게 되었다.
임스는 알고리즘 문제 출제 기준을 정하고자 한다.
임스가 N일 동안 푼 문제 중, 한국어로 이루어진 문제면서, 난이도가 3등급 이상인 문제들만 추천하고자 한다.
임스가 문제를 푼 일수 N과 해당 일수에 푼 문제들의 개수 A_i 가 주어진다.
이후에, 임스가 푼 문제에 대한 정보의 개수 M과 임스가 푼 문제에 대한 정보(언어와 등급, 개수)가 주어진다.
임스가 N일 동안 추천할 문제를 몇 문제 골랐는지 각 일자별로 출력하시오.

[입력]
가장 첫 번째 줄에는 테스트케이스 수 TC가 주어진다.
각 테스트케이스 첫 번째 줄에는 임스가 문제를 푼 일수 N (1 <= N <= 100) 이 주어진다.
두 번째 줄에는 임스가 해당 일수에 푼 문제들의 개수 A_i (1<= A_i <= 20) 이 공백을 기준으로 주어진다.
세 번째 줄에는 임스가 푼 문제들의 정보의 개수 M (1 <= M <= 100) 이 주어진다.
네 번째 줄부터 M줄에 거쳐 임스가 푼 문제의 정보가 주어진다.
언어는 ko와 en만 주어지고, 등급은 1 ~ 5까지 주어진다.

[출력]
각 케이스마다 '#t' (t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
임스가 N일 동안 고른 문제들을 일자별로 공백을 기준으로 나뉘어 출력한다.

[접근방법]
문제의 정보 중 숫자만큼 반복해서 큐에 더한다. 첫 번째 줄에 준 문제의 개수만큼 순회하면서 정답리스트 ans에 담는다.
'''
from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int,input().split()))
    M = int(input())
    problems = deque()
    for _ in range(M):
        problem = input().split()
        for i in range(int(problem[2])):
            problems.append(problem[:2])
    ans = [0] * N
    for i in range(N):
        for p in range(ls[i]):
            prob = problems.popleft()
            if prob[0]=='ko' and int(prob[1])>=3:
                ans[i] += 1
    print(f'#{tc}', *ans)
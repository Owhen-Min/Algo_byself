'''
### 문제
세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.
N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

### 문제 조건
첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수, C는 109보다 작거나 같은 음이 아닌 정수이다.
둘째 줄에 물건의 무게가 주어진다. 무게도 109보다 작거나 같은 자연수이다.

### 입력 예제
2 1
1 1
=> 3

### 접근 방법
재귀함수로 접근한다. 들어갈 수 있는 경우 들어간 경우와 안 들어간 경우를 둘다 시뮬레이션한 값을 리턴하고,
들어갈 수 없는 경우 안 들어간 경우를 시뮬레이션한 값을 리턴한다. 언제까지? i가 N에 도달할 때까지
근데 맨 처음에 물건들을 sort하면 더이상 들어갈 수 없을 때 바로 나올 수 있어서 좋을 듯
'''

n, c = map(int, input().split())
ls = sorted(map(int, input().split()))


def package(depth, weight):
    if depth == n:
        return 1
    elif weight + ls[depth] > c:
        return 1
    else:
        return package(depth + 1, weight + ls[depth]) + package(depth + 1, weight)


print(package(0, 0))
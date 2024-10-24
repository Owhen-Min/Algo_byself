'''
싸피란, 삼성의 SW 교육 경험과 고용노동부의 취업 지원 노하우를 바탕으로, 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램이다.
이번에 싸피에 재학생 신분이 아닌 문제 출제 위원으로 간 임스는 싸피생들을 위하여 알고리즘 문제를 준비하였다.
임스는 싸피 재학생들을 위해 다양한 분류의 문제들을 준비한 후, 출제할 문제들을 추리는 작업을 진행하고 있다.
임스는 다양한 문제들을 만든 후, 등급을 매겨 난이도를 조정하는 중이다.
등급이 같은 경우, 사전 순으로 정렬하여 출력하고자 한다.
임스를 도와 출제하고자 하는 문제들의 순서를 정해주자.

[입력]
가장 첫 번째 줄에는 테스트케이스 수 TC가 주어진다.
각 테스트케이스 첫 번째 줄에는 임스가 만든 문제의 수 N(1 <= N <= 100)이 주어진다.
그 다음 줄에는 N줄에 걸쳐 임스가 만든 문제(1<= 문자열 길이 <= 20)와 등급(1 <= 등급 <= 10) 이 공백을 기준으로 나뉘어 주어진다.

[출력]
각 케이스마다 '#t' (t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
임스가 출제하고자 하는 문제들을 순서대로 출력한다.

[접근방법]
리스트로 받은 후 key를 람다+sorted 함수를 사용해서 정렬한 뒤, 요소들만 별도의 리스트로 담아 언패킹해 출력한다.
'''


T= int(input())
for tc in range(1, T+1):
    n = int(input())
    ls = [0] * n
    for i in range(n):
        ls[i] = input().split()
    ans = [x[0] for x in sorted(ls, key=lambda x: (x[1],x[0]))]
    print(f'#{tc}', *ans)
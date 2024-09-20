from collections import deque
for _ in range(1, 11):
        t = int(input())                        # test case 호출용 변수
        dq = deque(map(int,input().split()))    # 받은 숫자를 dq에 덱의 형태로 저장
        while dq[-1] != 0:                      # dq의 마지막 숫자가 0일 때까지
            for i in range(1,6):                # 1~5까지의 한 사이클을 구현한다
                dq.append(dq.popleft()-i)       # dq의 제일 왼쪽 숫자에 i를 뺀 것을 제일 오른쪽에 더해준다
                if dq[-1] <= 0:                 # dq의 마지막 숫자가 0보다 같거나 작을 경우
                    dq[-1] = 0                  # dq의 마지막 숫자를 0으로 만들어준다.
                    break                       # cycle을 종료한다.
        print(f'#{t}', *dq)


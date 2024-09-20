def rcp(s,e):                           # 가위바위보 승패를 가르는 함수
    global b
    if RCPs[s]-RCPs[e] == 2 or  RCPs[s]-RCPs[e] == -2:
        if RCPs[s] == 3:
            b[e] = 1
            return e
        else:
            b[s] = 1
            return s

    elif RCPs[s]==RCPs[e]:
        b[s] = 1
        return s

    else:
        if RCPs[s]>RCPs[e]:
            b[s] = 1
            return s
        else:
            b[e] = 1
            return e


def torn(s,e):                        # 토너먼트 조를 나누는 함수
    global b
    if e-s == 0:                      # 1인 조의 경우 부전승
        b[e] = 1
        return e
    elif e-s == 1:                      # 2명인 경우, 가위바위보 승패를 가른다.
        return rcp(s, e)
    elif b[s] or b[e]:
        return rcp(s, e)
    else:
        return torn(torn(s, (e+s)//2), torn((e+s)//2+1, e))    # 2명 초과면, 조를 나눈다.


T= int(input())                         # 총 테스트 케이스
for tc in range(1, T+1):
    N = int(input())                    # 총 선수 수
    b = [0] * (N+1)
    RCPs = [0] + list(map(int,input().split()))   # 선수들의 가위바위보 값. 1번부터 N번까지의 인덱스 번호와 일치시키기 위해 0번에는 0 할당.
    print(f'#{tc} {torn(1,N)}')



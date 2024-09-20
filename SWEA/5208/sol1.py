# global 안쓰기

def min_charge(curr,cnt,fuel, min_cnt):
    # case 1. 현재까지 충전횟수가 최고 충전횟수보다 많을 경우, 나간다.
    if min_cnt < cnt:
        return min_cnt
    # case 2. 목적지에 도착했으면 최소 횟수를 갱신한다. 도착할 때 충전을 한다고 계산했으므로 cnt에서 1을 빼준다.
    elif curr == N-1:
        return cnt-1
    # case 3. 앞으로 갈 연료가 남아있다면, 남은 연료로 가장 멀리 가는 곳에서부터 충전하는 것을 계산한다.
    else:
        for i in range(fuel,0,-1):
            if curr+i <N:
                min_cnt = min_charge(curr+i,cnt+1,ls[curr+i] if curr+i < N-1 else 1, min_cnt)
        return min_cnt


T = int(input())
for tc in range(1, T+1):
    N, *ls = map(int,input().split())
    print(f'#{tc} {min_charge(0, 0, ls[0], N)}')
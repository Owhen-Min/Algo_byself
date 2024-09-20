T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int,input().split())
    cnt = 0
    if C < 3 or B < 2:
        result = -1
    else:
        while C <= B :
            B -= 1
            cnt +=1
        while B <= A:
            A -= 1
            cnt +=1
        result = cnt
    print(f'#{tc} {result}')
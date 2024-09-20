T = int(input())
decode_dict = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

for tc in range( 1, T+1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    pw = ''                             # pw를 담는 빈 str
    for i in range(N):
        for j in range(M-1,-1,-1):      # j를 뒤에서 탐색. 암호의 끝은 무조건 1이므로 뒤에서부터 탐색할 때 전체 암호를 얻을 수 있음.
            if mat[i][j]=='1':
                pw = mat[i][j-55:j+1]   # 1이 나온 자리부터 앞의 55개를 모두 pw에 담는다.
                break
        if pw: break                    # pw 값이 할당되었다면 반복문을 빠져나온다.

    code_sum = 0                        # 정답을 뽑기 위해 모든 자리의 숫자를 오롯이 더하는 변수 code_sum
    code_checker = 0                    # 올바른 암호문인지 체크하는 code_checker

    for i in range(8):
        code_sum += decode_dict[pw[i*7:i*7+7]]
        if i % 2:
            code_checker += decode_dict[pw[i*7:i*7+7]]
        else: code_checker += 3*decode_dict[pw[i*7:i*7+7]]

    print(f'#{tc} 0') if code_checker % 10 else print(f'#{tc} {code_sum}')
    # code_checker가 10으로 나눴을 때 나머지가 남아있다면 0을 출력, 아니라면 code_sum을 출력
    

char_dict = {
    '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
    '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
    '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
    'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'
}

decoder = {
    '3211' : 0, '2221' : 1, '2122' : 2, '1411' : 3, '1132' : 4,
    '1231' : 5, '1114' : 6, '1312' : 7, '1213' : 8, '3112' : 9
}

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = set()
    for _ in range(N):
        line = input().strip('0')
        if line: codes.add(line)
    print(codes)
    # idx = 0
    # while idx < len(codes):
    #     if len(codes[idx])%6
    #
    # overall_pw_sum = 0
    #
    # for code in codes:
    #     s = ''
    #     for char in code:
    #         s += char_dict[char]
    #     jump = len(s) // 56
    #
    #     ver_sik = 0
    #     pw_sum = 0
    #     for i in range(8):
    #         if i % 2: ver_sik += decoder[s[jump*7*i:jump*7*i+jump*7:jump]]
    #         else: ver_sik += 3* decoder[s[jump * 7 * i:jump * 7 * i + jump * 7:jump]]
    #         pw_sum += decoder[s[jump*7*i:jump*7*i+jump*7:jump]]
    #     if not ver_sik % 10:
    #         overall_pw_sum += pw_sum
    #
    # print(f'#{tc} {overall_pw_sum}')
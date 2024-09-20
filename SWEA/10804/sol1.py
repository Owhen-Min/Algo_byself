T = int(input())
dic= { 'b':'d',
       'p':'q',
       'q':'p',
       'd':'b'}
for tc in range(1, T+1):
    s = input()
    new_s = []
    for i in range(len(s)-1,-1,-1):
        new_s.append(dic[s[i]])
    print(f'#{tc} {"".join(new_s)}')
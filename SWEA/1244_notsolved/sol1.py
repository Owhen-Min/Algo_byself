T = int(input())
for tc in range(1, T+1):
    s, N = input().split()
    s= list(map(int,s))
    N = int(N)
    if len(s)-1 > N:
        for i in range(N):
            s_max = s[i]
            s_max_i = i
            for j in range(i+1, len(s)):
                if s[j] < s_min:
                    s_min = s[j]
                    s_min_i = j
                elif s[j] >= s_max:
                    s_max = s[j]
                    s_max_i = j
            s[s_min_i], s[s_max_i] = s[s_max_i], s[s_min_i]
        print(f'#{tc}', end= ' ')
        for c in s:
            print(c, end = '')
    else:
        s.sort()
        if (len(s)-1-N)%2 == 0:
            print(f'#{tc}', end= ' ')
            for c in s:
                print(c, end = '')
        else:
            s[-1], s[-2] = s[-2], s[-1]
            print(f'#{tc}', end= ' ')
            for c in s:
                print(c, end = '')
    print()
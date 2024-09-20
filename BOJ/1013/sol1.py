T = int(input())
for tc in range(T):
    radio = input()
    cursor = 0
    result = 'NO'
    N = len(radio)
    while cursor < N:
        if radio[cursor] == '0':
            cursor += 1
            if cursor < N and radio[cursor] == '1':
                cursor +=1
            else:
                break
        else:
            if cursor + 3 >= N:
                break
            else:
                for _ in range(2):
                    cursor+=1
                    if radio[cursor] == '1':
                        result = 'YES'
                if result == 'YES':
                    result = 'NO'
                    break

                while radio[cursor]=='0':
                    cursor += 1
                    if cursor == N:
                        break

                while cursor != N and radio[cursor] == '1':
                    cursor += 1

    else: result = 'YES'
    print(result)
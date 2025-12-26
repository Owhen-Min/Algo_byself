n = input()
ls = sorted(input().split(), key = lambda x: x*10, reverse=True)
if all(c == "0" for c in ls):
    print(0)
else:
    print(''.join(ls))
from collections import defaultdict

# print(ord('0')) // 48
# print(ord('A')) // 65

n = int(input())

# 해당 숫자를 Z로 바꿨을 때 추가될 값을 미리 계산해 담을 margin
margin = defaultdict(int)

def ternary_to_decimal(num:str) -> int:
    global margin
    value = 0
    leng = len(num)

    # 숫자 하나하나 변환
    for i in range(leng-1, -1, -1):
        curr_num = num[i]
        # 숫자일 경우
        if ord(curr_num)<65:
            v = int(curr_num)
            value += v*(36**(leng-i-1))
            # 해당 알파벳을 Z로 바꿨을 때 추가될 값을 미리 계산
            margin[curr_num] += (35-v)*(36**(leng-i-1))
        # 알파벳일 경우
        else:
            # A가 10이고, Z가 35이므로 ord에서 55를 차감함
            v = ord(curr_num)-55
            value += v * (36 ** (leng-i-1))
            # 해당 알파벳을 Z로 바꿨을 때 추가될 값을 미리 계산
            margin[curr_num] += (35 - v) * (36 ** (leng-i-1))

    return value

# 기존 값을 그대로 넣었을 때 합을 담는 변수 ans
ans = sum(ternary_to_decimal(input()) for _ in range(n))

# Z로 치환 가능한 알파벳을 크기 순서대로 내림차순으로 담은 list 할당. pop()으로 하나씩 뽑아올 것임
possible_alphabets = sorted(margin.keys(), key= lambda x: margin[x])

k = int(input())

# K개의 알파벳을 바꿀 때 최댓값부터 하나하나 바꾼다.
# K가 너무 클 경우를 대비해서 미리 조건문을 걸어둔다.
if k < len(margin):
    for _ in range(k):
        ans += margin[possible_alphabets.pop()]
else:
    ans += sum(margin.values())

def decimal_to_ternary(num:int) -> str:
    ans = ''
    while num >0:
        div, mod = divmod(num, 36)
        if mod<10:
            ans += str(mod)
        else:
            ans += chr(mod+55)
        num = div

    return ans[::-1] if ans else 0

print(decimal_to_ternary(ans))
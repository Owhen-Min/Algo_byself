from functools import cmp_to_key

n = int(input())
numbers = input().split()

# a+b와 b+a를 비교하여 정렬
def compare(a, b):
    if a + b > b + a:
        return -1  # a를 앞에
    elif a + b < b + a:
        return 1   # b를 앞에
    else:
        return 0

sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
result = ''.join(sorted_numbers)
print(int(result))
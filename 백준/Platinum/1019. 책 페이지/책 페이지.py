def count_digits(n):
    counts = [0] * 10
    length = len(str(n))

    for i in range(length):
        power = 10 ** (length - 1 - i)
        left = n // (power * 10)
        current = (n // power) % 10
        right = n % power

        for d in range(10):
            if d > 0:  # 1부터 9까지의 처리
                if current < d:
                    counts[d] += left * power
                elif current == d:
                    counts[d] += left * power + right + 1
                else:
                    counts[d] += (left + 1) * power
            else:  # 0의 처리 (Leading zeros 방지 로직 포함)
                if left > 0:  # 가장 앞자리가 아닐 때만 계산
                    if current == 0:
                        counts[d] += (left - 1) * power + right + 1
                    else:
                        counts[d] += left * power
                elif i > 0 and current > 0:  # 앞자리가 0인 경우는 pass
                    counts[d] += left * power

    return counts

def main():
    n = int(input())
    result = count_digits(n)
    print(*result)

main()
from collections import defaultdict
from math import gcd

def count_integer_product_pairs(N, numbers):
    # Convert floats to integers by multiplying with their denominators
    integers = []
    denominators = []
    for num in numbers:
        str_num = f"{num:.9f}"  # Convert to string with 9 decimal places
        denominator = 10 ** (len(str_num) - str_num.index('.') - 1)
        integer = int(num * denominator)
        integers.append(integer)
        denominators.append(denominator)

    # Count the frequency of each (numerator, denominator) pair
    freq = defaultdict(int)
    for i, d in zip(integers, denominators):
        g = gcd(i, d)
        freq[(i // g, d // g)] += 1

    # Count pairs that result in integer products
    count = 0
    for (n1, d1), f1 in freq.items():
        for (n2, d2), f2 in freq.items():
            if d1 * d2 == gcd(n1 * n2, d1 * d2):
                if (n1, d1) == (n2, d2):
                    count += f1 * (f1 - 1) // 2
                elif (n1, d1) < (n2, d2):
                    count += f1 * f2

    return count

# Read input and process test cases
T = int(input())
for _ in range(T):
    N = int(input())
    numbers = [float(input()) for _ in range(N)]
    result = count_integer_product_pairs(N, numbers)
    print(result)
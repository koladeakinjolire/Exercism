import math

def triplets_with_sum(number):
    triplets = []
    max_m = int(math.sqrt(number // 2)) + 1

    for m in range(2, max_m):
        for n in range(1, m):
            # Ensure primitivity: gcd(m, n) = 1 and exactly one of m or n is odd
            if math.gcd(m, n) == 1 and ((m % 2 == 1) != (n % 2 == 1)):
                denominator = 2 * m * (m + n)
                if number % denominator == 0:  # k must be an integer
                    k = number // denominator
                    x = k * (m * m - n * n)  # First leg
                    y = 2 * k * m * n        # Second leg
                    c = k * (m * m + n * n)  # Hypotenuse
                    # Ensure a < b < c by sorting the legs
                    a, b = min(x, y), max(x, y)
                    if a < b < c:  # Ensure ordering
                        triplets.append([a, b, c])

    return sorted(triplets)
number = 840
print(triplets_with_sum(number))
number = 108
print(triplets_with_sum(number))
number = 1000
print(triplets_with_sum(number))
number = 30000
print(triplets_with_sum(number))
number = 12
print(triplets_with_sum(number))
number = 90
print(triplets_with_sum(number))
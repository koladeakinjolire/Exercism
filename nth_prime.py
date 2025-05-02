def prime(number):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    if number < 1:
        raise ValueError("there is no zeroth prime")
    prime_list = []
    num = 2
    while len(prime_list) < number:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list[-1]



print(prime(5))
print(prime(1))
print(prime(6))
print(prime(10001))
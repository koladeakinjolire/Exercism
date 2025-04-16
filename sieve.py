import math
def primes(limit):
    if limit < 2:
        return []
        
    if limit == 2:
        return [limit]

    is_prime = [False, False] + [True] * (limit - 1)
    
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            for multiple in range(p*p, limit + 1, p):
                is_prime[multiple] = False
                
    prime_numbers = [i for i, prime in enumerate(is_prime) if prime]
    return prime_numbers

print(primes(500))
print(primes(13))
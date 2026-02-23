#!/usr/bin/env python3
"""Compute and print the first 100 prime numbers."""

def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        limit = int(candidate ** 0.5)
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


if __name__ == "__main__":
    primes = first_n_primes(100)
    print(*primes)
#!/usr/bin/env python3
"""Compute and print the first 100 prime numbers."""

def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        limit = int(candidate ** 0.5)
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


if __name__ == "__main__":
    primes = first_n_primes(100)
    print(*primes)

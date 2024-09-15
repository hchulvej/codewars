import gmpy2

def prime_gen():
    n = 2
    while True:
        yield n
        n = gmpy2.next_prime(n)


def solve(a, b):
    sum = 0
    primes = prime_gen()
    i = 1
    p = next(primes)
    while p <= b:
        if p >= a and gmpy2.is_prime(i):
            sum += p
        i += 1
        p = next(primes)
    return sum

print(solve(1, 10))
# kata: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4
def gap(g, m, n):
    def is_prime(x):
        if x % 2 == 0:
            return False
        for i in range(3,int(n**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True
    primes = []
    for i in range(m, n+1):
        if is_prime(i) and len(primes) < 2:
            primes.append(i)
        elif is_prime(i):
            if primes[1] - primes[0] == g:
                return [primes[0], primes[1]]
            else:
                primes.pop(0)
                primes.append(i)

    return [primes[0], primes[1]] if primes[1] - primes[0] == g else None


# kata: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4
def gap(g, m, n):
    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    prev_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if prev_prime is not None:
                if num - prev_prime == g:
                    return [prev_prime, num]
            prev_prime = num

    return None

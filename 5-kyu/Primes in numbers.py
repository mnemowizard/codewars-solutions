# kata: https://www.codewars.com/kata/54d512e62a5e54c96200019e
def prime_factors(n):
    if n == 1:
        return ''

    res = []
    divisor = 2

    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor

        if count > 0:
            res.append(f"({divisor})" if count == 1 else f"({divisor}**{count})")

        divisor += 1
        if divisor * divisor > n > 1:
            res.append(f"({n})")
            break

    return ''.join(res)
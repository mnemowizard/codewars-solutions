# kata: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n):
    multiply_num = lambda x: x if x < 10 else x%10 * multiply_num(x//10)
    res = 0
    while n > 9:
        n = multiply_num(n)
        res += 1

    return res


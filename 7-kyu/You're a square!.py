# kata: https://www.codewars.com/kata/54c27a33fb7da0db0100040e
def is_square(n):
    return n**(1/2) == int(n**(1/2)) if n > 0 else False
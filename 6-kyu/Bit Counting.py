# kata: https://www.codewars.com/kata/526571aae218b8ee490006f4/python
def count_bits(n):
    bits = list(str(bin(n)))
    return bits.count('1')

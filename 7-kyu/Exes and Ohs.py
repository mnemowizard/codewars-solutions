# kata: https://www.codewars.com/kata/55908aad6620c066bc00002a/python
def xo(s):
    lower_s = s.lower()
    return lower_s.count('o') == lower_s.count('x')
# kata: https://www.codewars.com/kata/54d4c8b08776e4ad92000835
import math

def isPP(n):
    for i in range(2, int(n**0.5) + 1):
        need_power = round(math.log(n, i), 10)
        if int(need_power) == need_power and need_power < n:
            return [i, int(need_power)]
    return None


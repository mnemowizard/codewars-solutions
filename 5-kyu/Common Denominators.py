# kata: https://www.codewars.com/kata/54d7660d2daf68c619000d95
import math

def convert_fracts(lst):
    denom = 1
    denoms = set(x[1] for x in lst)
    for i in denoms:
        denom = abs(denom * i) // math.gcd(denom, i)

    return [ [x[0]*int((denom/x[1])), denom] for x in lst]
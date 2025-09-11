# kata: https://www.codewars.com/kata/52efefcbcdf57161d4000091
def count(s):
    res = {}
    unique_s = set(s)
    for i in unique_s:
        res[i] = s.count(i)
    return res
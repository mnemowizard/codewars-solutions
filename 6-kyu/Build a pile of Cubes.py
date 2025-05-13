# kata: https://www.codewars.com/kata/5592e3bd57b64d00f3000047
def find_nb(m):
    mat = 0
    k = 1
    while mat <  m:
        mat += k**3
        k += 1
    else:
        if mat == m:
            return k - 1
        else:
            return -1
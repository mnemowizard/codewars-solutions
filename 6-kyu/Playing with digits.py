# kata: https://www.codewars.com/kata/5552101f47fc5178b1000050
def dig_pow(n, p):
    nk = sum(int(d)**(p+i) for i, d in enumerate(str(n)))
    k = nk/n

    return [-1, int(k)][k == int(k)]


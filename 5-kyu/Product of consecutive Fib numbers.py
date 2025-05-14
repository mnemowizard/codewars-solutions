# kata: https://www.codewars.com/kata/5541f58a944b85ce6d00006a/solutions/python
def product_fib(prod):
    res = [0,1]
    while res[0] * res[1] < prod:
        res[0] , res[1] = res[1], res[0] + res[1]
    else:
        if prod == res[0] * res[1]:
            return [res[0] , res[1] , True]
        else:
            return [res[0] , res[1] , False]
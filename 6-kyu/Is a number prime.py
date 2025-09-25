# kata: https://www.codewars.com/kata/5262119038c0985a5b00029f
def is_prime(num):
    if (num % 2 == 0 or num < 2) and num != 2:
        return False
    try:
        return next(False for i in range(3,int(num**0.5) + 1, 2) if num % i == 0)
    except StopIteration:
        return True
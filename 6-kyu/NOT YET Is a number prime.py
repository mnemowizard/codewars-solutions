# kata: https://www.codewars.com/kata/5262119038c0985a5b00029f
# Для решение нужно понять Тест Миллера-Рабина

from timer_decorator import timer
import random

@timer
def is_prime(num):
    pass
@timer
def is_prime2(num):
    if num <= 1:
        return False
    if num % 2 == 0 and num != 2:
        return False

    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True

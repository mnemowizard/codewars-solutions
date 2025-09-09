# kata: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
from timer_decorator import timer

def zeros(n):
    res = 0
    for i in range(0, n + 1, 5):
        while i % 5 == 0 and i > 9:
            i //= 5
            res += 1
        else:
            if i == 5:
                res += 1
    return res

@timer
def count_fives(start, end):
    count = 0
    fives = []
    for i in range(start, end, 5):
        five = [i,0]
        while i > 9 and i % 5 == 0:
            i //= 5
            count += 1
            five[1] += 1
        else:
            if i == 5:
                count += 1
                five[1] += 1
        fives.append(five)
    print(fives)
    return f'FIVES: {count}'

print(count_fives(0, 10))
print(count_fives(0, 101))
print(count_fives(0, 1001))
print(count_fives(0, 10001))
print(count_fives(0, 100001))
print(count_fives(0, 1000000001))
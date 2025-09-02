# kata: https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    max_min_nums = sorted(map(int, numbers.split(" ")))
    return '{} {}'.format(max_min_nums[-1], max_min_nums[0])
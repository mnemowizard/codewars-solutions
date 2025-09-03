# kata: https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers: list):
    is_outlier = int(integers[0]%2 == 0) + int(integers[1]%2 == 0) + int(integers[2]%2 == 0)
    if is_outlier > 1:
        return list(filter(lambda x: x%2 != 0, integers))[0]
    else:
        return list(filter(lambda x: x%2 == 0, integers))[0]



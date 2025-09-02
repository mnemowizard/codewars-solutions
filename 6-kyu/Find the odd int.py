# kata: https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq : list):
    checked_nums = []
    for num in seq:
        if num not in checked_nums:
            if seq.count(num) % 2 != 0:
                return num
    return None


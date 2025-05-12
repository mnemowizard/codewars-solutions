# kata: https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python
def find_next_square(sq):
    return [-1, int(pow(pow(sq, 1 / 2) + 1, 2))][pow(sq, 1 / 2) == int(pow(sq, 1 / 2))]
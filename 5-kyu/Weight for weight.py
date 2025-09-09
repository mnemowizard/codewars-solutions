# kata: https://www.codewars.com/kata/55c6126177c9441a570000cc
def order_weight(string):
    print(string)
    while '  ' in string:
        string = string.replace('  ', ' ')
    split_string = string.split()

    return ' '.join(sorted(sorted(split_string), key = lambda x: sum(map(int , x))))

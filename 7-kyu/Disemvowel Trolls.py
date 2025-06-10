# kata: https://www.codewars.com/kata/52fba66badcd10859f00097e
def disemvowel(string_):
    vowels = 'aAoOeEiIuU'
    for x in vowels:
        string_ = string_.replace(x, '')
    return string_
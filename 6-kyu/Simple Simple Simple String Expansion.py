# kata: https://www.codewars.com/kata/5ae326342f8cbc72220000d2
def string_expansion(s):
    rsl = ''
    for i, d in enumerate(s[0:-1]):
        if d.isdigit() and not s[i + 1].isdigit():

            rsl += s[i + 1] * int(d)
        elif not d.isdigit():

            rsl += d
    return rsl

print(string_expansion('3D2a5d2f'))
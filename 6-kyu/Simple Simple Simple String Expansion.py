# kata: https://www.codewars.com/kata/5ae326342f8cbc72220000d2
def string_expansion(s):
    res = ''
    count = 1
    for i in s:
        if i.isdigit():
            count = int(i)
        else:
            res += i*count
    return res

print(string_expansion('1111'))
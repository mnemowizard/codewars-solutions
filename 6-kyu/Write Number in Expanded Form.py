# kata: https://www.codewars.com/kata/5842df8ccbd22792a4000245
def expanded_form(num):
    res = []
    str_num = str(num)
    for i, d in enumerate(str_num):
        if d != '0': res.append( str(int(d) * 10**(len(str_num) - i - 1)) )

    return ' + '.join(res)


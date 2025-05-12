# kata: https://www.codewars.com/kata/55c45be3b2079eccff00010f
def order(sentence):
    if sentence == '':
        return ''
    result = ''
    lst = sentence.split()
    d = {int(n): st for st in lst for n in st if n.isdigit()}
    for i in sorted(d)[0:-1]:
        result += d[i] + ' '
    else:
        result += d[sorted(d)[-1]]
    return result
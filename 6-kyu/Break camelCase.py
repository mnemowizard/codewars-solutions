# kata: https://www.codewars.com/kata/5208f99aee097e6552000148/solutions/python
def solution(s):
    res = ''
    if s == '':
        return ''
    for i in range(0,len(s) - 1):
        if s[i+1].upper() == s[i+1]:
            res += s[i]
            res += ' '
        else:
            res += s[i]
    else:
        res += s[-1]
    return res
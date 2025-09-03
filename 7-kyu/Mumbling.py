# kata: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(st):
    res = ""
    for i, d in enumerate(st):
        append_chars = d.upper() + d.lower()*i
        if res:
            res += '-'
            res += append_chars
        else:
            res += append_chars
    return res
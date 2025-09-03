# kata: https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text: str):
    res = ""
    is_upper = False
    for i ,d in enumerate(text):
        if d in ['-', '_']:
            is_upper = True
        else:
            if is_upper:
                is_upper = False
                res += d.upper()
            else:
                res += d

    return "".join(res)


# kata: https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r, g, b):
    valid_num = lambda x: (0 if x < 0 else x) if x < 0 else (255 if x > 255 else x)
    r = f"{valid_num(r):X}".rjust(2, '0')
    g = f"{valid_num(g):X}".rjust(2, '0')
    b = f"{valid_num(b):X}".rjust(2, '0')

    return f"{r}{g}{b}"


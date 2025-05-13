# kata: https://www.codewars.com/kata/5277c8a221e209d3f6000b56
def valid_braces(string):
    open = []

    for v in string:
        if v == '(' or v == '{' or v == '[':
            open.append(v)
        else:
            if open == []:
                return False
            if v == ')':
                v = '('
            if v == ']':
                v = '['
            if v == '}':
                v = '{'
            if v == open[-1]:
                open.pop()

            else:
                return False
    else:
        if open:
            return False
        else:
            return True
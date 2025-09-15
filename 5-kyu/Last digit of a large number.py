# kata: https://www.codewars.com/kata/5511b2f550906349a70004e1
def last_digit(n1, n2):
    str_n1 = str(n1)
    if n2 == 0:
        return 1

    if str_n1[-1] == '0':
        return 0
    if str_n1[-1] == '1':
        return 1
    if str_n1[-1] == '2':
        if n2 % 4 == 1:
            return 2
        if n2 % 4 == 2:
            return 4
        if n2 % 4 == 3:
            return 8
        if n2 % 4 == 0:
            return 6
    if str_n1[-1] == '3':
        if n2 % 4 == 1:
            return 3
        if n2 % 4 == 2:
            return 9
        if n2 % 4 == 3:
            return 7
        if n2 % 4 == 0:
            return 1
    if str_n1[-1] == '4':
        if n2 % 2 == 1:
            return 4
        if n2 % 2 == 0:
            return 6
    if str_n1[-1] == '5':
        return 5
    if str_n1[-1] == '6':
        return 6
    if str_n1[-1] == '7':
        if n2 % 4 == 1:
            return 7
        if n2 % 4 == 2:
            return 9
        if n2 % 4 == 3:
            return 3
        if n2 % 4 == 0:
            return 1
    if str_n1[-1] == '8':
        if n2 % 4 == 1:
            return 8
        if n2 % 4 == 2:
            return 4
        if n2 % 4 == 3:
            return 2
        if n2 % 4 == 0:
            return 6
    if str_n1[-1] == '9':
        if n2 % 2 == 1:
            return 9
        if n2 % 2 == 0:
            return 1

# kata: https://www.codewars.com/kata/530e15517bc88ac656000716
def rot13(message):
    res = ""
    for i in message:
        ord_i = ord(i)
        if 65 <= ord_i <= 90:
            add = ord_i - 13 if ord_i + 13 > 90 else ord_i + 13
            res += chr(add)
        elif 97 <= ord_i <= 122:
            add = ord_i - 13 if ord_i + 13 > 122 else ord_i + 13
            res += chr(add)
        else:
            res += i

    return res


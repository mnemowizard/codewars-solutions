# kata: https://www.codewars.com/kata/520b9d2ad5c005041100000f
def pig_it(text):
    text_list = text.split()
    res = ""
    for i in text_list:
        if i.isalpha():
            res += i[1:] + i[0] + 'ay' + ' '
        else:
            res += i + ' '

    return res[0:-1]

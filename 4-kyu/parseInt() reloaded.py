# kata: https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
figures = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
others = ['hundred', 'thousand', 'million', 'and']


def convert_number(x, zeroes = 0):
    if x in figures:
        return figures.index(x) * (zeroes+1)
    elif x in teens:
        return (10 + teens.index(x)) * (zeroes+1)
    elif x in tens:
        return ((tens.index(x)+1)*10) * (zeroes+1)

def parse_int(string):
    result = 0
    number = string.split()
    add = 0
    zeroes = string.count('million')*6 + string.count('thousand')*3 + string.count('hundred')*2

    for i in number:
        if i == 'and':
            continue
        if '-' in i:
            i = i.split('-')
            add += convert_number(i[0]) + convert_number(i[1])
            if zeroes == 0:
                result += add
            continue
        if i not in others and zeroes == 0:
            result += convert_number(i)
        if i not in others:
            add += convert_number(i)
        elif i in others:
            if i == 'million':
                zeroes -= 6
                add *= 1000000
                result += add
                add = 0
                continue
            if i == 'thousand':
                zeroes -= 3
                add *= 1000
                result += add
                add = 0
                continue
            if i == 'hundred' and zeroes == 2:
                zeroes -= 2
                add *= 100
                result += add
                add = 0
                continue
            else:
                zeroes -= 2
                add *= 100

    return result
# kata: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
def check(f, n):
    if f[0] == "+":
        return n + int(f[1])
    elif f[0] == "-":
        return n - int(f[1])
    elif f[0] == "*":
        return n * int(f[1])
    elif f[0] == "/":
        return int( n / int(f[1]) )


def zero(f=0):
    if f == 0:
        return '0'
    else:
        return check(f, 0)


def one(f=0):
    if f == 0:
        return '1'
    else:
        return check(f, 1)


def two(f=0):
    if f == 0:
        return '2'
    else:
        return check(f, 2)


def three(f=0):
    if f == 0:
        return '3'
    else:
        return check(f, 3)


def four(f=0):
    if f == 0:
        return '4'
    else:
        return check(f, 4)


def five(f=0):
    if f == 0:
        return '5'
    else:
        return check(f, 5)


def six(f=0):
    if f == 0:
        return '6'
    else:
        return check(f, 6)


def seven(f=0):
    if f == 0:
        return '7'
    else:
        return check(f, 7)


def eight(f=0):
    if f == 0:
        return '8'
    else:
        return check(f, 8)


def nine(f=0):
    if f == 0:
        return '9'
    else:
        return check(f, 9)


def plus(f): return '+' + f  #


def minus(f): return '-' + f


def times(f): return '*' + f

def divided_by(f): return '/' + f


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
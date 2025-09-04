# kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(lst):
    no_zeros = []
    yes_zeros = []
    for i in lst:
        if i != 0:
            no_zeros.append(i)
        else:
            yes_zeros.append(i)

    return no_zeros + yes_zeros
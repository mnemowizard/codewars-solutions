# kata: https://www.codewars.com/kata/550498447451fbbd7600041c
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    temp = list(array2)

    for num in array1:
        square = num * num
        if square in temp:
            temp.remove(square)
        else:
            return False

    return len(temp) == 0


# kata: https://www.codewars.com/kata/550554fd08b86f84fe000a58
def in_array(array1, array2):
    return sorted([word for word in set(array1) if sum(1 for i in array2 if word in i) > 0])
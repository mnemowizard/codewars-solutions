# kata: https://www.codewarscodewars.com/kata/54521e9ec8e60bc4de000d6c
def max_sequence(arr):
    if not arr:
        return 0

    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
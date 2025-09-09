# kata: https://www.codewars.com/kata/5679aa472b8f57fb8c000047
def find_even_index(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        left_sum = 0
        right_sum = 0
        for j in range(len_arr):
            if j == i:
                continue
            elif j < i:
                left_sum += arr[j]
            else:
                right_sum += arr[j]
        if left_sum == right_sum:
            return i
    return -1
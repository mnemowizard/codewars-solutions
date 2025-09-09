# kata: https://www.codewars.com/kata/585d7d5adb20cf33cb000235
def find_uniq(arr):
    not_unique = int(arr[0] == arr[1]) + int(arr[0] == arr[2])
    if not_unique == 0:
        return not_unique
    elif not_unique == 1:
        return arr[1] if arr[0] != arr[1] else arr[2]
    else:
        for i in arr:
            if i != arr[0]:
                return i
        return None

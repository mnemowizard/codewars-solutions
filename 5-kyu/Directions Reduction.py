# kata: https://www.codewars.com/kata/550f22f4d758534c1100025a
def dir_reduc(arr):
    old_arr = None

    while old_arr != arr:
        old_arr = arr[:]
        for i, d in enumerate(arr[1:]):
            if d == 'NORTH':
                if arr[i] == 'SOUTH':
                    arr[i] = ''
                    arr[i+1] = ''

            elif d == 'SOUTH':
                if arr[i ] == 'NORTH':
                    arr[i] = ''
                    arr[i+1] = ''

            elif d == 'WEST':
                if arr[i] == 'EAST':
                    arr[i] = ''
                    arr[i+1] = ''

            else:
                if arr[i] == 'WEST':
                    arr[i] = ''
                    arr[i+1] = ''

        while '' in arr:
            arr.remove('')

    return arr


# kata: https://www.codewars.com/kata/583203e6eb35d7980400002a
def count_smileys(arr):
    count = 0
    for i in arr:
        if len(i) == 3:
            if i[0] in [':',';'] \
                and i[1] in ['-', '~'] \
                    and i[2] in [')','D']:
                count += 1
        else:
            if i[0] in [':',';'] \
                and i[1] in [')', 'D']:
                count += 1

    return count
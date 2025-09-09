# kata: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
def sort_array(source_array):
    odds = []
    for i in source_array:
        if i % 2 != 0:
            odds.append(i)
    else:
        odds = sorted(odds)

    k = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds[k]
            k += 1

    return source_array
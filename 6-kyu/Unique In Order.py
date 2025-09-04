# kata: https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(sequence):
    res = []
    for i in range(len(sequence)):
        if i != 0 and sequence[i] == sequence[i - 1]:
            continue
        else:
            res.append(sequence[i])

    return res
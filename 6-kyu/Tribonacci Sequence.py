# kata: https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(signature, n):
    res = []
    tribbo = signature[:]
    for i in range(n):
        if i < 3:
            res.append(signature[i])
        else:
            new_num = sum(tribbo)
            res.append(new_num)
            tribbo = tribbo[1:] + [new_num]
    return res
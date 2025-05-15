# kata: https://www.codewars.com/kata/5270d0d18625160ada0000e4/python
def score(dice):
    dic = dice[:]
    res = 0
    while dic:
        n = dic[0]
        if dic.count(n) >= 3:
            if n == 1:
                res += 1000
            else:
                res += n * 100
            dic.remove(n)
            dic.remove(n)
            dic.remove(n)
        elif n != 1 and n != 5:
            dic.remove(n)

        if dic.count(1) < 3 and dic.count(1) > 0:
            res += 100
            dic.remove(1)
        if dic.count(5) < 3 and dic.count(5) > 0:
            res += 50
            dic.remove(5)

    return res

print(score( [5, 3, 1, 1, 1] ))
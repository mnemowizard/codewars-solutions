# kata: https://www.codewars.com/kata/55aa075506463dac6600010d
import math

def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        sum_sq = 0

        for j in range(1, int(math.isqrt(i)) + 1):
            if i % j == 0:
                sum_sq += j * j
                if j != i // j:
                    sum_sq += (i // j) * (i // j)

        root = math.isqrt(sum_sq)
        if root * root == sum_sq:
            res.append([i, sum_sq])

    return res


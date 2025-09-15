# kata: https://www.codewars.com/kata/54d81488b981293527000c8f
def sum_pairs(ints: list, s: int):
    seen = set()
    for num in ints:
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None


print(sum_pairs( [1] * 1000000, 13))

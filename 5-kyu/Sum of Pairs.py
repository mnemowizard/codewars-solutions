# kata: https://www.codewars.com/kata/54d81488b981293527000c8f
def sum_pairs(ints: list, s: int):
    nums_pool = set()
    for num in ints:
        need_num = s - num
        if need_num in nums_pool:
            return [need_num, num]
        else:
            nums_pool.add(num)

    return None


print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
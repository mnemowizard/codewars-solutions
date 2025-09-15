# kata: https://www.codewars.com/kata/526989a41034285187000de4
def ips_between(start, end):
    res = 0
    start_list = list(map(int, start.split(".")))
    end_list = list(map(int, end.split(".")))
    for i in range(4):
        res += (end_list[3 - i] - start_list[3 - i])*(256**i)
    return res

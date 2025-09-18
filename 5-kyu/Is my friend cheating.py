# kata: https://www.codewars.com/kata/5547cc7dcad755e480000004
def remov_nb(n):
    res = []
    sum_n = sum(range(n+1))
    s = set()

    for i in range(n):
        if len(s) == 0:
            s.add(i)
        else:
            need_num = (sum_n - i)/(i+1)
            if need_num in s:
                res.append((int(need_num), i))
                res.append((i, int(need_num)))
            s.add(i)

    return sorted(res)

# kata: https://www.codewars.com/kata/5550d638a99ddb113e0000a2
def josephus(items : list, k: int):
    res = []
    index = 0
    while items:
        index = (index + k - 1) % len(items) if len(items) else len(items)
        res.append(items.pop(index))

    return res


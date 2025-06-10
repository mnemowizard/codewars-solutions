# kata: https://www.codewars.com/kata/554ca54ffa7d91b236000023/python
def delete_nth(order,max_e):
    new_order = order[::-1]
    for x in order:
        while new_order.count(x) > max_e:
             new_order.remove(x)
    return new_order[::-1]                
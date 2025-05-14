# put your python code here
def fast_sort(lst):
    if len(lst) > 2:
        mid = int(len(lst)/2)
        a = fast_sort(lst[0:mid])
        b = fast_sort(lst[mid:])
        c = []
        while a and b:
            for i in a:
                for j in b:
                    if i > j:
                        c.append(j)
                        b.remove(j)
                        break
                    else:
                        c.append(i)
                        a.remove(i)
                        break
                break
        if b:
            c += b
        if a:
            c += a
        return c
    elif len(lst) == 1:
        return lst.copy()
    else:
        return [min(lst),max(lst)]


lst = [int(x) for x in input().split()]
print(fast_sort(lst))

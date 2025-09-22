# kata: https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa
def choose_best_sum(t, k, ls):
    len_ls = len(ls)
    paths = []
    def funct(current_sum ,start, places):
        if places == 0:
            paths.append(current_sum)
            return None
        elif start > len_ls:
            return None
        else:
            for i in range(start, len_ls):
                if current_sum + ls[i] > t:
                    pass
                else:
                    funct(current_sum + ls[i], i + 1, places - 1)


    if k > len_ls:
        return None

    funct(0, 0, k)

    return sorted(paths)[-1] if paths else None



ts = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(230, 3, ts))
print('end')
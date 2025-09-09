# kata: https://www.codewars.com/kata/55c04b4cc56a697bb0000048
def scramble(s1, s2):
    replaced_chars = []
    for i in s1:
        if i in s2 and i not in replaced_chars:
            s2 = s2.replace(i, '', s1.count(i))
            replaced_chars.append(i)

    return not bool(s2)
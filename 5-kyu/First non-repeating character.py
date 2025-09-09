# kata: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
def first_non_repeating_letter(s):
    lower_s = s.lower()
    for i , d in enumerate(lower_s):
        if lower_s.count(d) == 1:
            return s[i]

    return ''